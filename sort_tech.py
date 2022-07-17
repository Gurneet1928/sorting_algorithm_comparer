import datetime as dt
import numpy as np
"""
a = dt.datetime.now()

b = dt.datetime.now()
time_diff = (b - a)
execution_time = time_diff.total_seconds() * 1000
return execution_time
"""
def selection_sort(A = [],*args):
    a = dt.datetime.now()
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    b = dt.datetime.now()
    time_diff = (b - a)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

def bubble_sort(A = []):
    a = dt.datetime.now()
    n=len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    b = dt.datetime.now()
    time_diff = (b - a)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

'''def insertion_sort(A=[],*args):
    
    a = dt.datetime.now()
    for i in range(1, len(A)):  
        value = A[i]  
        j = i - 1  
        while j >= 0 and value < A[j]:  
            A[j + 1] = A[j]  
            j = j - 1  
        A[j + 1] = value  
    b = dt.datetime.now()
    time_diff = (b - a)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)'''

def merge(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
  
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
  
def merge_sort(A=[],*args):
    B = A.copy()
    a = dt.datetime.now()
    width = 1    
    n = len(A)
    while (width < n):
        l=0
        while (l < n): 
            r = min(l+(width*2-1), n-1)         
            m = min(l+width-1,n-1)        
            merge(A, l, m, r)
            l += width*2
        width *= 2
    b = dt.datetime.now()
    time_diff = (b - a)
    if b==a:
        return merge_sort(B)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

def cocktail_sort(A=[]):
    B = A.copy()
    a = dt.datetime.now()
    n = len(A)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        start = start + 1
    b = dt.datetime.now()
    if b==a:
        return cocktail_sort(B)
    time_diff = (b - a)
    execution_time = time_diff.total_seconds() * 1000
    return execution_time

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
def heap_sort(A=[]):
    B=A.copy()
    a = dt.datetime.now()
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    b=dt.datetime.now()
    time_diff = (b-a)
    if b==a:
        return pigeon_hole_sort(B)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

def pigeon_hole_sort(A=[]):
    B=A.copy()
    a = dt.datetime.now()
    n = len(A)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        start = start + 1
    b=dt.datetime.now()
    time_diff = (b-a)
    if b==a:
        return pigeon_hole_sort(B)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

def gnome_sort(A=[]):
    B = A.copy()
    a = dt.datetime.now()
    index = 0
    n=len(A)
    while index < n:
        if index == 0:
            index = index + 1
        if A[index] >= A[index - 1]:
            index = index + 1
        else:
            A[index], A[index-1] = A[index-1], A[index]
            index = index - 1
    b = dt.datetime.now()
    if b==a:
        return gnome_sort(B)
    time_diff = (b - a)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

def shell_sort(A=[]):
    B=A.copy()
    a = dt.datetime.now()
    n = len(A)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        start = start + 1
    b = dt.datetime.now()
    time_diff = (b - a)
    if b==a:
        return shell_sort(B)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

def odd_even_sort(A=[],*args):
    B=A.copy()
    a = dt.datetime.now()
    n=len(A)
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                isSorted = 0
                  
        for i in range(0, n-1, 2):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                isSorted = 0
    b = dt.datetime.now()
    if b==a:
        return odd_even_sort(B)
    time_diff = (b - a)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)

def cycle_sort(A=[],*args):
    B = A.copy()
    a = dt.datetime.now()
    writes = 0
    for cycleStart in range(0, len(A) - 1):
        item = A[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, len(A)):
            if A[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == A[pos]:
            pos += 1
        A[pos], item = item, A[pos]
        writes += 1
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(A)):
                if A[i] < item:
                    pos += 1
            while item == A[pos]:
                pos += 1
            A[pos], item = item, A[pos]
            writes += 1
    b = dt.datetime.now()
    if b==a:
        return cycle_sort(B)
    time_diff = (b - a)
    execution_time = time_diff.total_seconds() * 1000
    return (execution_time)