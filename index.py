from flask import Flask, render_template,request


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

def create_output(category,rating,deal):
    url="https://www.amazon.in/gp/goldbox?gb_f_c2xvdC01=dealTypes:"
    string=''''''

    string+=str(deal[0])+'''<br>'''
    url+=str(deal[0])

    url+=",includedAccessTypes:KINDLE_CONTENT_DEAL,sortOrder:BY_SCORE,minRating:"

    url+=str(rating[0])
    string+=str(rating[0])+'''<br>'''

    url+=",enforcedCategories:"
    for i,cat in enumerate(category):
        string=string+str(cat)
        string+='''<br>'''
        url+=str(cat)
        if i<=len(category)-2:
            url+="%252C"

    with open('url.txt','w+') as f:
        f.write(url)

    string+='''<br><br> '''+url
    print(url)
    return string

@app.route('/showOutput', methods=['POST'])
def showOutput():
    return create_output(request.form.getlist('cat'),request.form.getlist('rating'),request.form.getlist('deal'))

if __name__ == '__main__':
    app.run()
