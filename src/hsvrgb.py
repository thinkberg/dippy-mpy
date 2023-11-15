def rgb565(red, green, blue):
    return (int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))


def hsv_to_rgb565(h: float, s: float, v: float) -> int:
    if s:
        if h == 1.0:
            h = 0.0
        i = int(h * 6.0)
        f = h * 6.0 - i

        w = int(255 * (v * (1.0 - s)))
        q = int(255 * (v * (1.0 - s * f)))
        t = int(255 * (v * (1.0 - s * (1.0 - f))))
        v = int(255 * v)

        if i == 0:
            return rgb565(v, t, w)
        if i == 1:
            return rgb565(q, v, w)
        if i == 2:
            return rgb565(w, v, t)
        if i == 3:
            return rgb565(w, q, v)
        if i == 4:
            return rgb565(t, w, v)
        if i == 5:
            return rgb565(v, w, q)
    else:
        v = int(255 * v)
        return rgb565(v, v, v)
