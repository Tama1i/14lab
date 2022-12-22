#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f():
    def g(x):
        return x + 3
 
    return g
 
 
k = int(input())
cnt = f()
print(cnt(k))
