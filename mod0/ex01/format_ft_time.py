import time

seconds = time.time()

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")

localtime = time.localtime()
print(f"{time.strftime('%b %d %Y', localtime)}")


