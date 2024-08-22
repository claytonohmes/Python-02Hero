def spy_game(nums):
    first0 = False
    second0 = False
    seven = False
    '''
    did this by accident for back to back
    for index in range(0,len(nums)):
        if nums[index] == 0 and nums[index+1] == 0 and nums[index+2] == 7:
            return True
        elif (len(nums) == index+2) and not (nums[index] == 0 and nums[index+1] == 0 and nums[index+2] == 7):
            return False
        else: pass
    '''
    sizeofls = len(nums) - 1
    for value in nums:
        print(value)
        if value == 0 and not first0 and not second0 and not seven:
            print('flag1')
            first0 = True
            pass
        elif value == 0 and first0 and not second0 and not seven:
            print('Flag2')
            second0 = True
            pass
        elif value == 7 and first0 and second0 and not seven:
            print('flag3')
            seven = True
            return True
        elif value != nums[sizeofls]:
            pass
        else:
            first0 = False
            second0 = False
            seven = False
    return False

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])