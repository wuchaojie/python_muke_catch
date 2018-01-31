#coding=utf-8

class HtmlOutputer(object):
    def __init__(self): 
        self.datas = []
    
    def collect_data(self,data):
#        print data
        if data is None :
            return
        self.datas.append(data)

    
    def output_html(self):
        fout=open('output.html','w')#输出到output.html中,w为写模式
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        print self.datas
        #ASCI
        for data in self.datas:
            print data["summary"]
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"].encode("UTF-8"))
            fout.write("<td>%s</td>" % data["summary"].encode("UTF-8"))
            fout.write("</tr>")
        
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
        
    def output_txt(self):
        
        with open('output.txt', 'w') as f:
            for data in self.datas:
                print data["summary"]
    
                f.write("URL地址:%s" % data["url"]+ "\n")
                f.write("标题Title:%s" % data["title"].encode("UTF-8")+ "\n")
                f.write("内容:%s" % data["summary"].encode("UTF-8")+ "\n")     

