#!/usr/bin/env python3

class Shoe:
    
    def __init__(self , brand , size ):
        self.brand = brand
        if isinstance(size, int):
            self.size = size
        else:
         raise ValueError("size must be an integer")

stan_smith = Shoe("Adidas", 9)


