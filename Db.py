from app import db, BlogPost

result = BlogPost.query.all()[0].date_post
print(result)
# db.session.add(BlogPost(title='Blog Post 2', content='Content No', author='Green'))
# db.session.commit()
