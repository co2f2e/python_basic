age = int(input('请输入你的年龄：'))
has_resport = input('你是否提交了体检报告？（是/否）')
level = int(input('请输入你的会员等级（1/2/3）'))
print('***********程序的识别结果如下**************')
if 18 <= age <= 45:
    print('你的年龄符合比赛要求')
    if has_resport == '是':
        print('你已提交体检报告！')
        print('你可以参加比赛！')
        if level == 1:
            print(f'尊敬的{level}会员，比赛结束后，你可以领取纪念T恤一件！')
        elif level == 2:
            print(f'尊敬的{level}会员，比赛结束后，你可以领取专业跑鞋一双！')
        elif level == 3:
            print(f'尊敬的{level}会员，比赛结束后，你可以领取运动耳机一副！')
        else:
            print('你输入的会员等级不正确！')
    elif has_resport == '否':
        print('你未提交体检报告，不能参加比赛！')
    else:
        print('你输入的体检报告有误！')
else:
    print('抱歉，参数年龄需要在18到45之间！')
