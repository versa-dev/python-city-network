def solution(front, back):
  distance = [0] * (len(front)-1)
  before = []
  for i in range(len(front)):
    if (front[i] == back[i]):
      before.append(back[i])
  
  num = 1
  index = 0
  array = []

  while(num < len(front)):
    
    for i in range(len(front)):
      for item in before:
        if (back[i] == item and back[i] != front[i]):
          array.append(front[i])
          distance[index] += 1
          num += 1
        
    index += 1
    before = array
    array = []

  return distance

I = input("Input the numbers: ")
N = input("Input the next cities: ")
Index = I.split(",")
Next = N.split(",")
print(solution(Index, Next))