def httpStatus(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(httpStatus(200))
print(httpStatus(404))
print(httpStatus(500))
print(httpStatus(999))