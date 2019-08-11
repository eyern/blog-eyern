from app.models import Review,User
from app import db

def tearDown(self):
        Review.query.delete()
        User.query.delete()
def test_check_instance_variables(self):
        self.assertEquals(self.new.user.blog_id,12345)
        self.assertEquals(self.new.user.blog_title,'Review for blog')
        self.assertEquals(self.new.user.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new.user.blog_review,'This blog is the best thing since sliced bread')
        self.assertEquals(self.new.user.user,self.user_oruko)        

def test_get_review_by_id(self):

        self.new.user.save_blog()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)