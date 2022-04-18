import sys
import pandas as pd


def main(data_json):
    '''
    Read collected news as a dict objects list
    '''

    with open(data_json, 'r') as read_file:
        lines = read_file.readlines()
        data_list = []
        for line in lines:
            data_list.append( eval(line)  )

        print(data_list)
        print('Size of data_list:', len(data_list))
        #print('View the first record:', data_list[0]['title'], data_list[0]['up_datetime'], data_list[0]['content'] )
        ####################################################
        # do something using your data
        begindf = pd.DataFrame(data_list, columns = ['url' , 'title', 'category', 'up_datetime', 'content'])
        return  begindf.to_csv('week5.csv')
main('/Users/wen/Desktop/時事關鍵字分析/chinatimes/chinatimes/spiders/2022041114_HW_2_begin.json') # change json file address while change file

#if __name__ == "__main__":
    #if (len(sys.argv) < 2):
        #print("Usage: %s <json file>"%sys.argv[0])
        #sys.exit(1)

    #if sys.argv[1]:
        #main(sys.argv[1])

