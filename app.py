from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template('index.html')

def bubble(li):

    for i in range(len(li)):
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
    print(li)
                
    return li 

def selection(li):
   
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
                li[j] = li[i]
                li[i], li[j] = li[j], li[i]

    return li

def insertion(li):
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            while li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li

def shell(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap // 2
    return arr

@app.route('/',methods=['POST'])
def task():
	if request.method == 'POST':
            li = str(request.form['input'])
            li = list(li.split(" "))
            req = request.form['task']
            operations = {
                '1': bubble(li),
                '2': selection(li),
                '3': insertion(li),
                '4': shell(li)
            }
            result = operations.get(req)
            return render_template('output.html', result = result)
if __name__ == '__main__':
    app.run()
