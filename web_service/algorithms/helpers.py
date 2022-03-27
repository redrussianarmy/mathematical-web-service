def prepare_response(res):
    if isinstance(res, int):
        return {
            "result": res
        }
    return None
