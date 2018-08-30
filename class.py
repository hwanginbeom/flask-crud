import datetime

class Post:
    db=[]
    
    @classmethod
    def dball(cls):
        for data in cls.db:
            print(data.title)
            
    def __init__(self,title,content): # init 문법 / self 는 자기 자신 (this 같은 것)
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()
        Post.db.append(self)
        
        
    def get(self):
        print("제목 : {}, 내용: {}".format(self.title,self.content))
        #print("제목 : {1}, 내용: {0}".format(self.title,self.content))
        #print("제목 : {title}, 내용: {contene}".format(title = self.title,content= self.content))
    
    def update(self,title=None,content=None):
        self.title = title  if title is not None else self.title
        self.content = content if content is not None else self.content
        print("글이 수정되었습니다.")
        
    def __del__(self):
        print("글이 삭제 되었습니다.")
                        # 개발자가 주로씀 이것을 바꾸면 str과 repr 둘다 바뀌고 
    def __repr__(self): # 오버라이딩 인데 사용자가 <__main__.Post object at 0x7fd694c9a2b0> 이걸 프린트 하면 이렇게 나온다.
        return '''       
        제목 : {}
        내용 : {}
        '''.format(self.title,self.content) # 주소를 부르는건가 ? 
                        # 사용자가 주로 쓰는데 str은 repr을 참조한다.
    def __str__(self): # 오버라이딩 인데 사용자가 <__main__.Post object at 0x7fd694c9a2b0> 이걸 프린트 하면 이렇게 나온다.
        return '''
        제목 : {}
        내용 : {}
        '''.format(self.title,self.content) # 주소를 부르는건가 ? 

def main():
    p1=Post("1번글" , "1번 제목")
    p2=Post("2번글" , "2번 제목")
    p3=Post("3번글" , "3번 제목")
    Post.dball()
    # p1.get()
    # p2.get()
    # p1.update("1번제목")
    print(p1)

if __name__ == "__main__":
    main()