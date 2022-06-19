from django.test import TestCase

from .models import *

# Create your tests here.
class PostTestClass(TestCase):
    def setUp(self):
        self.profile = Profile('8',fullname='isaac kiptoo',username='kiptoo',neighbourhood='Elgon view',email='mugera@gmail.com',proc_img='isaac.png',bio='am i a tm',contacts='0712345678',locations='Eldoret')
        self.profile.save_profile()


        self.business = Business(business_name='Bookshop')
        self.business.save_business()

        self.neighbourhood = NeighbourHood('8',neighbourhood_name='Elgon view',location='Eldoret',user='Mugera',hood_img='isaac.png',Occupants_Count='2',admin='admin',helpline='0712345678',description='the image is in good condition')
        self.neighbourhood.save_neighbourhood()

        self.initial_test= Post(title='Test',user='isaac',post_img='isaac.png',  description='the image is in good condition',created_at='25-04-2022',profile=self.profile,business=self.business,neighbourhood=self.neighbourhood )

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.initial_test,Post))

    # Testing the saved methods
    def test_saved_method(self):
        self.initial_test.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)



    def test_delete_post(self):
        self.initial_test.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)==0)

    def test_update_post(self):
        self.initial_test.save_post()
        self.initial_test.update_post(self.initial_test.id, 'images/test.jpg')
        new_post = Post.objects.filter(post='images/test.jpg')
        self.assertTrue(len(new_post)>0)

    # def test_search_by_title(self):
    #     self.initial_test.save_post()
    #     posts = self.initial_test.search_by_title(search_term='creativity')
    #     self.assertTrue(len(posts) ==0)



    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()
        Business.objects.all().delete()
        NeighbourHood.objects.all().delete()

class BusinessTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.business = Business(business_name='Bookshop')
        self.business.save_business()

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_rate(self):
        self.business.delete_rate()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)


   
    
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.profile = Profile('8',fullname='isaac kiptoo',username='kiptoo',neighbourhood='Elgon view',email='mugera@gmail.com',proc_img='isaac.png',bio='am i a tm',contacts='0712345678',locations='Eldoret')
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        profiless = Profile.objects.all()
        self.assertTrue(len(profiless) == 0)


class NeighbourHoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.neighbourhood = NeighbourHood('8',neighbourhood_name='Elgon view',location='Eldoret',user='Mugera',hood_img='isaac.png',Occupants_Count='2',admin='admin',helpline='0712345678',description='the image is in good condition')
        self.neighbourhood.save_neighbourhood()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, NeighbourHood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_neighbourhood()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    def test_delete_neighbourhood(self):
        self.neighbourhood.delete_neighbourhood()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods) == 0)

