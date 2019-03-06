""" 2'ye 2'lik matrisin determinandı. """

def determinand_2_by_2 (u):
  return u[0][0]*u[1][1] - u[0][1]*u[1][0]

""" 3'e 3'lük matris determinandı. """

def delete_row_col_from_matrix(u,m,n):
  result=[]
  size=len(u)
  size_2=len(u[0])
  for i in range(size):
    if(i==m):
      continue
    row_1=[]
    for j in range(size_2):
      if(j==n):
        continue
      row_1.append(u[i][j])
    result.append(row_1)
  return result


def determinand_3_by_3(u):
  a_1=u[0][0]
  a_2=delete_row_col_from_matrix(u,0,0)
  a_3=determinand_2_by_2(a_2)
  a_4=a_1*a_3

  b_1=u[0][1]
  b_2=delete_row_col_from_matrix(u,0,1)
  b_3=determinand_2_by_2(b_2)
  b_4=b_1*b_3

  c_1=u[0][2]
  c_2=delete_row_col_from_matrix(u,0,2)
  c_3=determinand_2_by_2(c_2)
  c_4=c_1*c_3 

  return a_4-b_4+c_4 

def determinand_from_4_by_4(u):

  a_1=u[0][0]
  a_2=delete_row_col_from_matrix(u,0,0)
  a_3=determinand_3_by_3(a_2)
  a_4=a_1*a_3

  b_1=u[0][1]
  b_2=delete_row_col_from_matrix(u,0,1)
  b_3=determinand_3_by_3(b_2)
  b_4=b_1*b_3

  c_1=u[0][2]
  c_2=delete_row_col_from_matrix(u,0,2)
  c_3=determinand_3_by_3(c_2)
  c_4=c_1*c_3 

  d_1=u[0][3]
  d_2=delete_row_col_from_matrix(u,0,3)
  d_3=determinand_3_by_3(d_2)
  d_4=d_1*d_3

  return a_4-b_4+c_4-d_4


matrix_3=[[1,2,3,4],[5,6,7,8],[9,10,11,15],[16,17,18,19]]
matrix_2=[[3,2,1],[3,4,2],[1,5,2]]
matrix_1=[[1,2],[3,4]]
print(determinand_2_by_2(matrix_1))
print(determinand_3_by_3(matrix_2))
print(determinand_from_4_by_4(matrix_3))


