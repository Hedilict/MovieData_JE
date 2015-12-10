def md5(value):
    import hashlib
    if isinstance(value, str):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()
    else:
        return ''

if __name__ == '__main__':
    print(md5('admin'))
