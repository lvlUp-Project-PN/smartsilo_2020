import json


class JSONConvert:

    @staticmethod
    def serialize(entity:object):
        return json.dumps(entity)

    @staticmethod
    def deserialize(json_str:str,entity:object):
        json_dict = json.loads(json_str)
        tmp_inst = entity()
        for key in json_dict.keys():
            if key in tmp_inst.__dict__.keys():
                tmp_inst.__dict__.update({key:json_dict[key]})
            else:
                pass
        return tmp_inst