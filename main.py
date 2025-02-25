import os
import subprocess

try:
    import numpy
    import customtkinter
except ImportError:
    print("Installing missing dependencies...")
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

import charPoly
from customtkinter import *



def init():
    global matrixA,matrixB,matrixC,mat1_size, result_matrix
    for i in matrix1.winfo_children():
        i.destroy()
    for i in matrix2.winfo_children():
        i. destroy()
    for i in result_matrix.winfo_children():
        i.destroy()
    matrixA = [CTkEntry(matrix1, width=2, placeholder_text="0") for i in range(mat1_size ** 2)]
    for i in range(mat1_size):
        for j in range(mat1_size):
            matrixA[(mat1_size * i + j)].grid(row=i, column=j)

    matrixB = [CTkEntry(matrix2, width=2, placeholder_text="0") for i in range(mat1_size ** 2)]
    for i in range(mat1_size):
        for j in range(mat1_size):
            matrixB[(mat1_size * i + j)].grid(row=i, column=j)

    matrixC = [CTkEntry(result_matrix, width=2, state="disabled", placeholder_text="0") for i in range(mat1_size ** 2)]
    for i in range(mat1_size):
        for j in range(mat1_size):
            matrixC[(mat1_size * i + j)].grid(row=i, column=j)

def change_operation(self):
    global selected_operation, calculate_button
    funcs={"*":times, "+":plus, "-":minus, "<>":inner_product, "determinant":calc_det, "characteristic polynomial":calc_charPoly}
    init()
    calculate_button.configure(command=funcs[selected_operation.get()])

def change_size(size):
    global mat1_size
    mat1_size = int(size.split("x")[0])
    init()

def sum_vects(num1, num2,mat1_vals, mat2_vals):
    global matrixA, matrixB, mat1_size
    sum =0
    for k in range(mat1_size):
        sum += int(mat1_vals[num1][k])*int(mat2_vals[k][num2])
    return sum

def times():
    global matrixA, matrixB, mat1_size, matrixC, result_matrix, ip_result
    matC_vals=calc_times(read_matrix(matrixA), read_matrix(matrixB))
    for i in range(mat1_size):
        for j in range(mat1_size):
            matrixC[mat1_size * i + j].configure(state="normal")
            matrixC[mat1_size * i + j].insert(0, str(matC_vals[i][j]))
            matrixC[mat1_size * i + j].configure(state="disabled")
            result_matrix.update()
    ip_result.grid_remove()
    result_matrix.grid(row=0, column=4)
    for i in range(mat1_size):
        for j in range(mat1_size):
            matrixC[(mat1_size * i + j)].grid(row=i, column=j)

def calc_times(mat1, mat2):
    global matrixA, matrixB, mat1_size, matrixC, result_matrix
    matA_vals = mat1
    matB_vals = mat2
    matC_vals = [[sum_vects(i, j, matA_vals, matB_vals) for j in range(mat1_size)] for i in range(mat1_size)]
    return matC_vals

def plus():
    global matrixA, matrixB, mat1_size, matrixC, result_matrix, ip_result
    matA_vals=read_matrix(matrixA)
    matB_vals=read_matrix(matrixB)
    matC_vals=[[int(matA_vals[i][j])+int(matB_vals[i][j]) for j in range(mat1_size)] for i in range(mat1_size)]
    print(matC_vals)
    ip_result.grid_remove()
    result_matrix.grid(row=0, column=4)
    for i in range(mat1_size):
        for j in range(mat1_size):
            matrixC[mat1_size * i + j].configure(state="normal")
            matrixC[mat1_size*i+j].insert(0,str(matC_vals[i][j]))
            matrixC[mat1_size * i + j].configure(state="disabled")
            result_matrix.update()

def minus():
    global matrixA, matrixB, mat1_size, matrixC, result_matrix
    matA_vals = read_matrix(matrixA)
    matB_vals = read_matrix(matrixB)
    matC_vals = [[int(matA_vals[i][j]) - int(matB_vals[i][j]) for j in range(mat1_size)] for i in range(mat1_size)]
    print(matC_vals)
    ip_result.grid_remove()
    result_matrix.grid(row=0, column=4)
    for i in range(mat1_size):
        for j in range(mat1_size):
            matrixC[mat1_size * i + j].configure(state="normal")
            matrixC[mat1_size * i + j].insert(0, str(matC_vals[i][j]))
            matrixC[mat1_size * i + j].configure(state="disabled")
            result_matrix.update()

def read_matrix(mat):
    global mat1_size
    mat_values = [[(mat[j*mat1_size+i].get()if(mat[j*mat1_size+i].get()) else 0) for i in range(mat1_size)] for j in range(mat1_size)]
    return mat_values

def transpose(mat):
    matA_vals=read_matrix(mat)
    matA_vals=[[matA_vals[i][j] for i in range(mat1_size)] for j in range(mat1_size)]
    return  matA_vals

def inner_product():
    global matrixA, matrixB, ip_result, result_matrix

    matprod = calc_times(transpose(matrixA), read_matrix(matrixB))
    print(trace(matprod))
    for w in ip_result.winfo_children():
        w.destroy()
    ip_result.grid(row=0, column=4)
    result_matrix.grid_remove()
    ip_res_num = CTkLabel(ip_result, text=str(trace(matprod)))
    ip_res_num.pack()

def trace(mat):
    global mat1_size
    return sum([int(mat[i][i]) for i in range(mat1_size)])

def switch():
    global matrixA, matrixB, mat1_size
    for i in range(mat1_size**2):
        v1=matrixA[i].get() if matrixA[i].get() else 0
        v2=matrixB[i].get() if matrixB[i].get() else 0
        matrixA[i].delete(0,END)
        matrixB[i].delete(0,END)
        matrixA[i].insert(0, v2)
        matrixB[i].insert(0,v1)
    root.update()

def determinant(mat, size):
    det=0
    if size==1:
        return int(mat[0][0])
    if size ==2:
        return int(mat[0][0])*int(mat[1][1])-int(mat[0][1])*int(mat[1][0])
    else:

        for i in range(size):
            det += ((-1) ** (i+1)) * (int(mat[size - 1][i + 1]) if i != (size - 1) else 0) * determinant(mat, size - 1)

        return det

def calc_det():
    global matrixA, matrix2, mat1_size, root, result_matrix,matrixC, ip_result
    det = determinant(read_matrix(matrixA), mat1_size)
    for w in ip_result.winfo_children():
        w.destroy()
    for w in matrix2.winfo_children():
        w.configure(state="disabled")
    ip_result.grid(row=0, column=4)
    result_matrix.grid_remove()
    ip_res_num = CTkLabel(ip_result, text=str(det))
    ip_res_num.pack()

def calc_charPoly():
    global matrixA, matrix2, mat1_size, root, result_matrix, matrixC, ip_result
    det = charPoly.characteristic_polynomial(read_matrix(matrixA))
    for w in ip_result.winfo_children():
        w.destroy()
    for w in matrix2.winfo_children():
        w.configure(state="disabled")
    ip_result.grid(row=0, column=4)
    result_matrix.grid_remove()
    ip_res_num = CTkLabel(ip_result, text=str(det))
    ip_res_num.pack()



root = CTk()
#root.geometry("600x400")

matrix1 = CTkFrame(root)
matrix1.grid(row=0,column=0, padx=5, pady=80)
mat1_size=3


operations=["*", "+", "-", "<>", "determinant", "characteristic polynomial"]
selected_operation = StringVar(value="operation")

dropdown = CTkComboBox(root, values=operations, variable=selected_operation, command = change_operation, font=("arial", 7*mat1_size))
dropdown.grid(row=0, column=1)

matrix2 = CTkFrame(root)
matrix2.grid(row=0,column=2, padx=5)

sizes=[f"{i}x{i}" for i in range(1, 11)]
mat_size=IntVar(value=3)

mat_size_selector = CTkComboBox(root, values=sizes, variable=mat_size, command=change_size)
mat_size_selector.grid(row=1, column=2)

equals_label =CTkLabel(root, text="=", font=("arial", 10*mat1_size))
equals_label.grid(row=0, column=3)

result_matrix = CTkFrame(root)
result_matrix.grid(row=0,column=4, padx=5)

ip_result = CTkFrame(root)


matrixA=[CTkEntry(matrix1, width=2,placeholder_text="0") for i in range(mat1_size**2)]
for i in range(mat1_size):
    for j in range(mat1_size):
        matrixA[(mat1_size*i+j)].grid(row=i, column=j)

matrixB=[CTkEntry(matrix2, width=2,placeholder_text="0") for i in range(mat1_size**2)]
for i in range(mat1_size):
    for j in range(mat1_size):
        matrixB[(mat1_size*i+j)].grid(row=i, column=j)


matrixC=[CTkEntry(result_matrix, width=2, state="disabled",placeholder_text="0") for i in range(mat1_size**2)]
for i in range(mat1_size):
    for j in range(mat1_size):
        matrixC[(mat1_size*i+j)].grid(row=i, column=j)


calculate_button = CTkButton(root, text="calculate",width=10, command=lambda: print(read_matrix(matrixA)))
calculate_button.grid(row=1, column=1)


exchange_button = CTkButton(root, text="⇆", command=switch)
exchange_button.grid(row=2, column=1)
print(read_matrix(matrixA))
print(determinant(read_matrix(matrixA), mat1_size-1))
print(charPoly.characteristic_polynomial(read_matrix(matrixA)))



root.mainloop()
