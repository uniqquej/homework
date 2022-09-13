def calc(prob):
   
    nums = []
    op = []

    for i in range(len(prob)):
        if (i % 2 == 0) | (i == 0):
            x = int(prob[i])
            nums.append(x)
        else:
            op.append(prob[i])
    
    total = nums[0]

    for j in range(len(nums)-1):
    
        if op[j] == '+':
            result = total + nums[j+1]
        elif op[j] == '-':
            result = total - nums[j+1]
        elif op[j] == '*':
            result = total * nums[j+1]
        elif op[j] == '/':
            result = total / nums[j+1]
        
        total = result

    return result