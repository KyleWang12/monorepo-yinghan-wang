import json

class ExtendedEncoder(json.JSONEncoder):

    def default(self, o):
        name = o.__class__.__name__
        try:
            encoder = getattr(self, f'encode_{name}')
        except AttributeError:
            return super().default(o)
        else:
            encoded = encoder(o)
            encoded["__extended_json_type__"] = name
            return encoded
        
    def encode_complex(self, o):
        return {"real": o.real, "imag": o.imag}
    
    def encode_range(self, o):
        return {"start": o.start, "stop": o.stop, "step": o.step}


class ExtendedDecoder(json.JSONDecoder):

    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, o):
        try:
            name = o["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return o
        else:
            return decoder(o)
        
    def decode_complex(self, o):
        return complex(o["real"], o["imag"])
        
    def decode_range(self, o):
        return range(o["start"], o["stop"], o["step"])
    

if __name__ == "__main__":
    # Test
    data = {
        "a": complex(1, 2),
        "b": range(10, 20, 2),
        "c": "Hello World!"
    }
    json_data = json.dumps(data, cls=ExtendedEncoder)
    print(json_data)
    decoded_data = json.loads(json_data, cls=ExtendedDecoder)
    print(decoded_data)
    print(type(decoded_data["a"]))
    print(type(decoded_data["b"]))
    print(type(decoded_data["c"]))