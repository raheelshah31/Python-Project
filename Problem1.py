
dict = {}  # empty dictionary
dict[0] = 0
dict[1] = 3
dict[2] = 3
dict[3] = 5
dict[4] = 4
dict[5] = 4
dict[6] = 3
dict[7] = 5
dict[8] = 5
dict[9] = 4
dict[10] = 3
dict[11] = 6
dict[12] = 6
dict[13] = 8
dict[14] = 8
dict[15] = 7
dict[16] = 7
dict[17] = 9
dict[18] = 8
dict[19] = 8
dict[20] = 6
dict[30] = 6
dict[40] = 5
dict[50] = 5
dict[60] = 5
dict[70] = 7
dict[80] = 6
dict[90] = 6
dict[100] = 7
dict[1000] = 11
words = {}  # empty dictionary of words
words[0] = 0
words[1] = 'One'
words[2] = 'Two'
words[3] = 'Three'
words[4] = 'Four'
words[5] = 'Five'
words[6] = 'Six'
words[7] = 'Seven'
words[8] = 'Eight'
words[9] = 'Nine'
words[10] = 'Ten'
words[11] = 'Eleven'
words[12] = 'Twelve'
words[13] = 'Thirteen'
words[14] = 'Fourteen'
words[15] = 'Fifteen'
words[16] = 'Sixteen'
words[17] = 'Seventeen'
words[18] = 'Eighteen'
words[19] = 'Nineteen'
words[20] = 'Twenty'
words[30] = 'Thirty'
words[40] = 'Fourty'
words[50] = 'Fifty'
words[60] = 'Sixtey'
words[70] = 'Seventy'
words[80] = 'Eighty'
words[90] = 'Ninety'
words[100] = 'Hundred'
words[1000] = 'Thousand'
sum = 0

# sumation for single digit numbers

for i in range(1, 11):
    sum += dict[i]
    print (words[i], '', 'Sum=', sum)

# summation for numbers less than 20

for i in range(11, 21):
    sum += dict[i]
    print (words[i], '', 'Sum=', sum)

# for sumation upto hundred terms

for i in range(21, 100):
    j = i
    sum += dict[j - j % 10]
    sum += dict[j % 10]
    print (words[j - j % 10], words[j % 10], '', 'Sum=', sum)
sum += dict[1] + dict[100]
print (words[100], '', 'Sum=', sum)

# for numbers from 101 to 999

for i in range(101, 1000):

        # print("sum = "+str(sum)+" i = "+str(i))

    sum += dict[int(i / 100)] + dict[100]

    try:
        if dict[i % 100] == 0:
            print (
                words[int(i / 100)],
                ' ',
                words[100],
                '',
                'Sum=',
                sum,
                )
            pass
        else:
            sum += len('and')
            sum += dict[i % 100]
            print (
                words[int(i / 100)],
                ' ',
                words[100],
                'and',
                ' ',
                words[i % 100],
                '',
                'Sum=',
                sum,
                )
    except Exception:

           # print("Teen Number Detected in 100s ")
           # print(dict[i%100])

        sum += len('and')
        sum += dict[i % 100 - i % 10] + dict[i % 10]
        print (
            words[int(i / 100)],
            ' ',
            words[100],
            'and',
            str(words[i % 100 - i % 10]),
            ' ',
            str(words[i % 10]),
            '',
            'Sum=',
            sum,
            )
        pass

sum += dict[1000]
print (words[1000], '', 'Sum=', sum)
print 'Total = %d' % sum

input('That was Awesome :)')


			
