def division_eu(a:int, b:int) -> tuple:
    """renvoie la division euclidienne de a et b avec b supposé non nul"""
    q, r = 0, a
    while r >= b:
        q, r = q+1, r-b
    return q, r