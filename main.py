# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:53:22 2022

@author: Sayantan
"""

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pickle
import random
import pandas as pd
import requests
from functools import lru_cache
import urllib.request
import re



           
def main():
    st.markdown("""<style> p {
                            text-align: center};
                            </style>""", unsafe_allow_html=True)
    st.markdown(""" <style> img {
         border-radius:10px; 
         } </style> """, unsafe_allow_html=True)
                            
    
                                
    #INITIALISING SESSION STATE VARIABLES 
    if 'drama' not in st.session_state:
        st.session_state.drama = 0
    if 'comedy' not in st.session_state:
        st.session_state.comedy = 0
    if 'thriller' not in st.session_state:
        st.session_state.thriller = 0
    if 'animation' not in st.session_state:
        st.session_state.animation = 0
    if 'romance' not in st.session_state:
        st.session_state.romance = 0
    if 'family' not in st.session_state:
        st.session_state.family = 0
    if 'scifiction' not in st.session_state:
        st.session_state.scifiction = 0
    if 'action' not in st.session_state:
        st.session_state.action = 0

    if 'profile_content_recommendations' not in st.session_state:
        st.session_state.profile_content_recommendations = []
    if 'movie_key' not in st.session_state:
        st.session_state.movie_key = 0
        
    if 'profile_buzzfeed_recommendations' not in st.session_state:
        st.session_state.profile_buzzfeed_recommendations = []
    if 'buzzfeed_key' not in st.session_state:
        st.session_state.buzzfeed_key = 0
        
    #FUNCTION TO GET THE YOUTUBE TRAILER URL
    @lru_cache(maxsize=10)
    def play_yt_video(selected_movie_name):
        search_keyword = selected_movie_name+"trailer"
        search_keyword = search_keyword.replace(" ", "+")
        html = urllib.request.urlopen(
            "https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        
        # Get URL for the first search result in Youtube
        yt_link = "https://www.youtube.com/watch?v=" + video_ids[0]
        return yt_link
        
    
    #USER SEARCH DISPLAY DATA
    def profile_data(poster_link,num):
           
           if num==0:
               st.session_state.movie_key+=1
               st.session_state.profile_content_recommendations.append({"movie_key": st.session_state.movie_key, "link": poster_link})
               
           elif num==1:
               st.session_state.buzzfeed_key+=1
               st.session_state.profile_buzzfeed_recommendations.append({"buzzfeed_key": st.session_state.buzzfeed_key, "link": poster_link})
             
    #IMPORTING PICKLE FILES
    # movies_dict = pickle.load(open('Pickle-files/movies_dict.pkl', 'rb'))
    # movies = pd.DataFrame(movies_dict)
    
    # similarity = pickle.load(open('Pickle-files/similarity.pkl', 'rb'))
    
    # ratings_dict = pickle.load(open('Pickle-files/ratings.pkl', 'rb'))
    # ratings = pd.DataFrame(ratings_dict)

    # books_dict = pickle.load(open('Pickle-files/books_dict.pkl', 'rb'))
    # books = pd.DataFrame(books_dict)

    # book_images_dict = pickle.load(open('Pickle-files/book_images_dict.pkl', 'rb'))
    # book_images = pd.DataFrame(book_images_dict)

    # quiz_data = pickle.load(open('Pickle-files/quiz_data.pkl', 'rb'))
    # quiz = pd.DataFrame(quiz_data)
    
    # user_rating_movie_dict = pickle.load(open('Pickle-files/user_rating_movie.pkl', 'rb'))
    # user_rating_movie = pd.DataFrame(user_rating_movie_dict)

    
    logo = Image.open(r'Images/logo.png')
    
    #CREATING WEBSITE'S MAIN NAVBAR
    with st.sidebar:
        choose = option_menu(menu_title="FOOD RECOMMENDATION SYSTEM", options=["Buzz-inga","Result"],
                             icons=['house-fill', 'bookmark-heart', 'kanban',
                                    'book', 'patch-question-fill', 'pin-map-fill', 'save2'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
                                 "menu-title": {"color": "orange"},
            "container": {"padding": "5!important", "background-color": "#00000"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"color": "orange", "background-colour": "red", "font-size": "16px", 
                         "text-align": "left", "margin": "0px", "--hover-color": "#fae5df"},
            "nav-link-selected": {"background-color": "#fae5df"},
        }
        )

    
    
    
    
    
    
    if choose == "About":
        st.markdown("""<style> p {
                            text-align: left; font-size:18px; }
                        h3{text-align:center; font-size: 27px; color:#ed7966; background-color:#f5cac2; font-family:'georgia' }
            
                            </style>""", unsafe_allow_html=True)
                        
                            
        col1, col2 = st.columns([0.2, 0.8])
        
        with col1:               
            st.image(logo, width=130 )
        st.write("Welcome to my recommendation engine! This engine has 5 major recommendation features-")
        
        st.subheader("Movie recommendation- content based filtering")
        st.write("Choose your preferred movie and the number of recommendations you require to get the movie recommendations based on genre, cast members and storyline.")
        
        st.subheader("Movie recommendation- collaborative based filtering")
        st.write("Rate movies out of 5 and we'll recommend movies based on user similarity. You can rate as many movies as you like to get more precise recommendations!")
        
        st.subheader("Cross Recommendation (Books)")
        st.write("Name your favourite movie and leave the responsibility of getting the perfect book recommendation on us.",
                 "Perfect opportunity to begin your reading journey or save the hassle of finding the next perfect read.")
        
        st.subheader("ai-chef")
        st.write("Inspired from Buzzfeed quizzes, Buzz-inga has quirky questions from your preferred food item to your favourite meme.",
                 "Answer under the four sections in Buzz-inga and we'll figure out your movie liking according to your mood and state of mind.")
        
        st.subheader("Map")
        st.write("From Parasite to Spider Man, we'll checklisted all. Time to do the same for our regional movies too.",
                 "Select any state on the Indian map and we'll direct you to the best feature movies of the area.")
        
      
        with col2:               
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}  </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">INTRODUCTION</p>',unsafe_allow_html=True)

        





    #RECOMMENDING MOVIES BASED ON CONTENT RECOMMENDATION (MATCHING GENRE, CAST NAME, STORYLINE)
    elif choose == "Food Recommendation":        
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">MOVIE RECOMMENDATION</p>', unsafe_allow_html=True)
        
        st.markdown(""" <style> img {
        height:300px; width: 300px} 
        </style> """, unsafe_allow_html=True)
    
        st.markdown(""" <style> code {
        color='pink'} 
        </style> """, unsafe_allow_html=True)

        
        #FUNCTION TO GET MOVIE POSTER FOR THE RECOMMENDED MOVIE
        def fetch_poster(movie_id):
            url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
                movie_id)
            data = requests.get(url)
            data = data.json()  # ???
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        
        
        #FUNCTION TO FIND THE RECOMMENDED MOVIE ACCORDING TO THE MOVIE NAME PROVIDED
        @lru_cache(maxsize=3)
        def recommend_movie(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]

            #Getting the top 5 movies based on distance
            movies_list = sorted(list(enumerate(distances)),
                                 reverse=True, key=lambda x: x[1])[1:6]
            movies_list_final = []
            
            #Getting the top recommendations considering the votes 
            for count, ele in movies_list:
                ele = ele * movies['vote_average'][count]
                temp = [count, ele]
                movies_list_final.append(temp)

            movies_list_final.sort(reverse=True, key=lambda x: x[1])

            recommended_movies = []
            recommended_movies_posters = []
            accuracy = []

            for i in movies_list_final:
                movie_id = movies.iloc[i[0]].id
                accuracy.append(i)
                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            
            #Sending the top movie recommendation to the profile's page
            profile_data(recommended_movies_posters[0],0)
            return recommended_movies, recommended_movies_posters, accuracy    

        st.write("Search for your favourite movie and select the number of recommendations you need.")
        st.write("")
        
        selected_movie_name = st.selectbox(
            'SEARCH FOR YOUR FAVOURITE MOVIE!', movies['title'].values)

        number_of_recommendations = st.selectbox(
            'NUMBER OF RECOMMENDATIONS NEEDED', (1, 2, 3))
        
        if st.button('Recommend'):
            names, posters, accuracy = recommend_movie(selected_movie_name)
            
            if number_of_recommendations == 1:
                st.markdown(""" <style> h2 {text-align:center}</style>""", unsafe_allow_html=True)
                st.header(names[0])
                col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                col2.image(posters[0],use_column_width=True)
               
                #st.image(posters[0])
                
                if(accuracy[0][1] > 2):
                    st.code("ACCURACY MATCH: 100%")
                else:
                    text="ACCURACY MATCH:"+ str(round((accuracy[0][1]-1)*100,2))+ "%"
                    st.code(text)
                    
                with st.expander("PLAY THE TRAILER"):
                    yt_link = play_yt_video(names[0])
                    st.video(yt_link)
            


            elif number_of_recommendations == 2:
                col1, col2 = st.columns(2)
                with col1:
                    st.write()
                    st.subheader(names[0])
                    st.image(posters[0])
                    
                    if(accuracy[0][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[0][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[0])
                        st.video(yt_link)

                with col2:
                    st.subheader(names[1])
                    st.image(posters[1])
                    if(accuracy[1][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[1][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[1])
                        st.video(yt_link)
           
            elif number_of_recommendations == 3:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.text(names[0])
                    st.image(posters[0])
                    
                    if(accuracy[0][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[0][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[0])
                        st.video(yt_link)

                with col2:
                    st.text(names[1])
                    st.image(posters[1])
                    
                    if(accuracy[1][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[1][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[1])
                        st.video(yt_link)

                with col3:
                    st.text(names[2])
                    st.image(posters[2])
                    
                    if(accuracy[2][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[2][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[2])
                        st.video(yt_link)








    #RECOMMENDING MOVIES BASED ON USER RATINGS (FINDING SIMILARITIES AMONG USERS- COLLABORATIVE FILTERING)
    elif choose == "User Ratings":
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">COLLABORATIVE FILTERING</p>',
                    unsafe_allow_html=True)
        
        st.markdown(""" <style> h3 {
        text-align: center;} 
        </style> """, unsafe_allow_html=True)
    
        
        st.write("Rate the movies (out of 5) according to your taste and we'll take care of the rest! To get your top recommendations",
                 ", select the option of not rating the movies further.")
        #FUNCTION TO GET SIMILARITY SCORES BASED ON USER RATINGS
        def get_similar_movies(movie_name, user_rating):
            similar_score = ratings[movie_name]*(user_rating-2.5)
            similar_score = similar_score.sort_values(ascending=False)
            return similar_score


        i = 0
        option = []
        while i < 10:
            option.append(random.randrange(0, 4))
            i += 1


        user_ratings = []

        #FUNCTION TO PRINT THE STARS BASED ON USER RATINGS
        @lru_cache(maxsize=3)
        def get_stars(score):
            if score == 1:
                return "⭐"
            elif score == 2:
                return "⭐⭐"
            elif score == 3:
                return "⭐⭐⭐"
            elif score == 4:
                return "⭐⭐⭐⭐"
            elif score == 5:
                return "⭐⭐⭐⭐⭐"
            
            
        #FUNCTION TO PRINT THE MOVIE NAME AND IT'S RATING THAT USER ADDED
        @lru_cache(maxsize=3) 
        def show(movie, score):
            a = [movie, score]
            user_ratings.append(a)
            if(score > 0):
                string = movie+"         " + get_stars(score)
                show_ratings.append(string)


        i = 0
        x = 0
        flag = 0
        f = 0
        show_ratings = []
        for x in range(500):
            movie1 = user_rating_movie[0][x]
            with st.expander(movie1):
                score = st.number_input('INSTERT NUMBER', 0, 5, 0, 0, key=x)
                show(movie1, score)

            if(x % 10 == 0 and x != 0):
                st.subheader("YOUR MOVIE RATINGS:")
                for i in show_ratings:
                    st.write(i)
                option = st.selectbox('Want to rate more movies?', ('', 'Yes, why not', 'Nope'), key=x)
                if(option == 'Yes, why not'):
                    continue
                elif(option == 'Nope'):
                    f = 1
                    break
                else:
                    f = 0
                    break
            x += 1
            

        flag = 1
        similar_movies = pd.DataFrame()
        if(flag == 1 and f == 1):
            for movie, rating in user_ratings:
                similar_movies = similar_movies.append(
                    get_similar_movies(movie, rating), ignore_index=True)
            st.subheader("TOP 5 MOVIE RECOMMENDATIONS:")
            st.write(similar_movies.sum().sort_values(ascending=False)[:5])
           







    #RECOMMENDING BOOKS BASED ON USER'S FAVOURITE MOVIE(CROSS RECOMMENDATION)
    elif choose == "Cross Recommendation":
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">BOOK RECOMMENDATION</p>',
                    unsafe_allow_html=True)
        
        #STYLING 
        st.markdown("""<style> 
                        img{
                            height:300px
                            };
                        </style>""", unsafe_allow_html=True
                )
        
        #FUNCTION TO GIVE BOOK RECOMMENDATION BASED ON USER'S FAVOURITE MOVIE
        @lru_cache(maxsize=3)
        def recommend_book(movie):
            if movie not in books['title'].unique():
                movie_index = movies.loc[movies['title'] == movie].index[0]
                maxi = 0
                book_index = 0
                num = 0
                list2 = movies['genres'][movie_index]
                
                for i in books.index:
                    list1 = books['genre'][i]
                    num = len(set(list1) & set(list2))
                    
                    if num > maxi:
                        maxi = num
                        book_index = i
                
                name = books['title'][book_index]
                
                if (book_images['name'] == name).any():
                    book_image_index = book_images[book_images['name']== name].index[0]
                    link = book_images['l'][book_image_index]
                
                elif(books['author'][book_index]=="Tyler Edwards"):
                    link="https://images-eu.ssl-images-amazon.com/images/I/51I89NSwLGL._SX342_SY445_QL70_ML2_.jpg"
                    
                elif(books['author'][book_index]=="David Dennis"):
                    link="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1354880275l/16240980.jpg"
                    
                else:
                    link = "https://pbs.twimg.com/media/DL-ORRkVAAEey8m.jpg"

                author = books['author'][book_index]
                goodreads_link = books['book_link'][book_index]
                pages = books['num_of_page'][book_index]
                rating = books['rate'][book_index]
                return link, author, goodreads_link, rating, pages


            else:
                book_index = books.loc[books['title'] == movie].index[0]
                book_image_index = book_images.loc[book_images['name']
                                                   == movie].index[0]
                author = books['author'][book_index]
                link = book_images['l'][book_image_index]
                goodreads_link = books['book_link'][book_index]
                pages = books['num_of_page'][book_index]
                rating = books['rate'][book_index]
                return link, author, goodreads_link, rating, pages

        selected_movie_name = st.selectbox(
            'SEARCH FOR YOUR MOVIE HERE!', movies['title'].values)
        
        
        if st.button('Recommend'):
            link, author, goodreads_link, rating, pages = recommend_book(
                selected_movie_name)
            
            with st.expander("*Drumroll*    Your book recommendation is ready!"):
                if(link!="https://pbs.twimg.com/media/DL-ORRkVAAEey8m.jpg"):
                    col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                    col2.image(link, caption="Novel Coverpage", use_column_width=True)
                else:
                    st.image(link, caption="Novel Coverpage")
                st.write(author)
                st.write("RATING: ", rating)
                st.write("CHECK OUT THE BOOK: ", goodreads_link)
                st.write("NUMBER OF PAGES: ", pages)





    

    elif choose == "Buzz-inga":

        st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633; text-align:center;} 
            </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">AI-Chef By Cognozire</p>', unsafe_allow_html=True)

        st.markdown('<p>Attempt 3 Options from each category and move to result Tab.</p>', unsafe_allow_html=True)

        #STYLING
        st.markdown("""<style> img {
                            height: 250px};
                            </style>""", unsafe_allow_html=True
                    )
        st.markdown("""<style> button {
                            margin-left:100px
                              position: relative;
                              left: 2000px;
                            </style>""", unsafe_allow_html=True
                    )
        st.markdown(""" <style> .question_font {
            font-size:18px ; font-family: 'Spade'; border-radius: 5px; padding:10px; text-align: center; color: red; background-colour: white} 
            </style> """, unsafe_allow_html=True)
        
        choose = option_menu(menu_title=None, options=["FILMY", "CUISINE", "CHOICES", "MEMES", "RESULTS"],
                             #icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                             default_index=0,
                             orientation="horizontal"
                             )

        if choose=='FILMY':

            col1, col2 = st.columns(2)

            # THRILLER
            list1 = ["Frankly, my dear, I don't give a damn." ,
                     "Every lie we tell incurs a debt to the truth. Sooner or later, that debt is paid.",
                    "I am the one who knocks - Breaking Bad",
                     "You’d be surprised what even a good man is capable of in the right situation.",
                     "You better wake up. The world you live in is just a sugarcoated topping. There is another world beneath it, the real world. And if you want to survive it, you better learn to pull the trigger.",
                     "See, I’m not a monster. I’m just ahead of the curve.",
                     "He’s Not A Hero. He’s A Silent Guardian, A Watchful Protector. A Dark Knight",
                     "Winter is coming - Game of Thrones",
                     "The world is not just black or white, there's a lot of grey"]
            # ANIMATION
            list2 = ["Anderson, don’t talk out loud. You lower the IQ of the whole street",
                    "Virgil:'You think you have a chance here? I have an army.' Sam: 'Oh, yeah? Well, I’ve got my mom.'",
                     "I'm not a hero. I'm a high-functioning alcoholic and I'm a selfish prick",
                     "I am not a thing, I'm not a genre, I'm not a concept. I'm a person",
                     "You don't have to be blood to be family",
                     "Houston, we have a problem.",
                     "ADVENTURE IS OUT THERE",
                     "Jesse, you asked me if I was in the meth business or the money business… Neither. I’m in the empire business.",
                     "I’m only brave enough when I have to be. Being brave doesn’t mean you go looking for trouble.",
                     "There is no secret ingredient. It’s just you."]


            st.markdown('<h1 class="question_font">OH SO FILMY..</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)

            with st.container():
                with col1:
                    st.write(random.choice(list1))
                    if(st.button('DIALOGUE1')):
                        st.session_state.thriller+=1


                with col2:
                    st.write(random.choice(list2))
                    if(st.button('DIALOGUE2')):
                        st.session_state.animation+=1


          
        if choose=='CUISINE':
        # ROMANCE
            list1 = ["https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dinner-ideas-for-two-french-onion-soup-1641934966.jpg",
                     "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dinner-ideas-for-two-shrimp-scampi-1641934138.jpg?crop=0.906xw:0.906xh;0.0390xw,0.0625xh&resize=480:*",
                     "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/romantic-dinner-ideas-rigatoni-with-chicken-broccoli-and-bolognese-1609185894.jpg?crop=0.544xw:0.816xh;0,0.184xh&resize=480:*",
                     "https://content3.jdmagicbox.com/comp/def_content/coffee_shops/default-coffee-shops-7.jpg",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8N3R9OEOE8jrW12CTcpwlhmbyd2JZ-YYxQA&usqp=CAU",
                     "https://www.chefworks.com.au/assets/images/blog/most-popular-cafe-foods-2020/Cafe_Burger.jpg",
                     "https://i.pinimg.com/736x/7e/19/45/7e19458b55c8eecde96da947cba2200b.jpg",
                     "https://media.istockphoto.com/photos/margherita-pizza-picture-id1359188521?b=1&k=20&m=1359188521&s=170667a&w=0&h=4cVc9DGaS2eU56QAAXoVCU5BPmuULNMTKPZVJbdEuKc=",
                     "https://bellyfull.net/wp-content/uploads/2020/08/Omelette-blog-3-500x500.jpg",
                     "https://thumbs.dreamstime.com/b/breakfast-french-toast-indian-pakistani-food-bread-tea-breakfast-french-toast-indian-pakistani-food-bread-tea-189702044.jpg"]
            # FAMILY
            list2 = ["https://b.zmtcdn.com/data/pictures/9/19451479/4d73622168afc1c628bf7bad5802fd56.jpg?fit=around|771.75:416.25&crop=771.75:416.25;*,*",
                     "https://static.toiimg.com/thumb/53110049.cms?width=1200&height=900",
                     "https://i.ytimg.com/vi/3dWf6BNZPfo/maxresdefault.jpg",
                     "https://rookiewithacookie.com/wp-content/uploads/2020/05/IMG_2570.jpg",
                     "https://i.ndtvimg.com/i/2017-10/diwali-food-menu_620x350_71507898681.jpg",
                     "https://pipingpotcurry.com/wp-content/uploads/2020/11/Dosa-recipe-plain-sada-dosa-Piping-Pot-Curry.jpg",
                     "https://b.zmtcdn.com/data/pictures/chains/2/47572/6d88abe04745826ed75c704c02581742_featured_v2.jpg",
                     "https://sallysbakingaddiction.com/wp-content/uploads/2013/04/triple-chocolate-cake-4.jpg",
                     "https://curlytales.com/wp-content/uploads/2017/06/Shiv-Mishthan-Bhandar.jpg",
                     "https://i0.wp.com/Tropicsgourmet.com/wp-content/uploads/2015/10/indian-sweet-371357_1920.jpg"]

            st.markdown(""" <style> .question_font {color: green} </style> """, unsafe_allow_html=True)


            st.markdown('<h1 class="question_font">FEED ME PLEASE...</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with st.container():
                with col1:
                    link = random.choice(list1)
                    st.image(link, width=300)
                    if(st.button('BON APPETIT!')):
                        st.session_state.romance+=1

                with col2:
                    link = random.choice(list2)
                    st.image(link, width=300)

                    if(st.button('YUMMM')):
                        st.session_state.family+=1
                    st.text("")
         
        
        if choose=='CHOICES':

                # SCIFICTION
            list1 = ["https://storage.googleapis.com/gweb-uniblog-publish-prod/images/sleep-01.max-1000x1000.png",
                     "https://images.everydayhealth.com/images/emotional-health/meditation/a-complete-guide-to-meditation-722x406.jpg",
                     "https://images.ctfassets.net/81iqaqpfd8fy/41KiNVEWQM6MgY8QEGkoco/44b9952239085ad2c731b3dcef4cc94f/selfcareguide-02.jpg?h=620&w=1440",
                     "https://thumbs.dreamstime.com/b/angry-arguing-couple-people-shouting-vector-illustration-husband-wife-blaming-each-other-problem-man-woman-quarreling-212871922.jpg",
                     "https://www.rp-assets.com/images/news/2020/01/24/74412-large.jpeg",
                     "https://ggie.berkeley.edu/wp-content/uploads/2019/09/Listening_to_Music_Mindfully_1200x630.jpg",
                     "https://www.parkavepd.com/wp-content/uploads/2019/01/Park-View-Pediatric-7-Ways-To-Make-Brushing-Teeth-Fun-For-Your-Child.jpg",
                     "https://www.petmd.com/sites/default/files/styles/article_image/public/going-for-a-walk-picture-id917875026.jpg?itok=egUc9l-k",
                     "https://www.thesprucecrafts.com/thmb/4krlR_ONU4EDXKbCb8FCWFkz--Y=/2121x1414/filters:fill(auto,1)/GettyImages-922707682-5b90467bc9e77c0025931eef.jpg",
                     "https://www.mountainjobs.com/wp-content/uploads/2021/05/pexels-andre-furtado-2916820-750x458.jpg"]
            # ACTION
            list2 = ["https://thumbs.dreamstime.com/b/kids-play-football-child-soccer-field-outdoor-stadium-children-score-goal-game-little-boy-kicking-ball-school-172305207.jpg",
                     "https://m.economictimes.com/thumb/msid-89199209,width-1200,height-900,resizemode-4,imgsize-51168/working-out-in-the-gym.jpg",
                     "https://www.euston96.com/wp-content/uploads/2019/09/Horse-riding.jpg",
                     "https://media.istockphoto.com/vectors/children-dancing-vector-id939153522?k=20&m=939153522&s=612x612&w=0&h=taiOnstHlJbwXhqahfSuiStk2W_ZYEGf0diYEVkuxbs=",
                     "https://images.pexels.com/photos/2889491/pexels-photo-2889491.jpeg?cs=srgb&dl=pexels-brady-knoll-2889491.jpg&fm=jpg",
                     "http://www.popcornoncouch.com/wp-content/uploads/2016/05/cinemaaudience.jpg",
                     "https://im.rediff.com/news/2019/oct/16khandu1.jpg?w=670&h=900",
                     "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y29va2luZyUyMGhvbWV8ZW58MHx8MHx8&w=1000&q=80",
                     "https://media.istockphoto.com/photos/young-woman-making-bed-at-home-picture-id1138390931?k=20&m=1138390931&s=612x612&w=0&h=of1Asq66j4sa4cTSywHwz5bCmRfTPFZG1_q3pmOxjRE=",
                     "https://www.kevinandamanda.com/wp-content/uploads/2021/12/G0056963-720x960.jpg"]

            st.markdown(""" <style> .question_font {color: orange} </style> """, unsafe_allow_html=True)


            st.markdown('<h1 class="question_font">LIFE CHOICES...</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with st.container():
                with col1:
                    link = random.choice(list1)
                    st.image(link, width=300)
                    if(st.button('TEAM LEFT')):
                        st.session_state.scifiction += 1
                with col2:
                    link = random.choice(list2)
                    st.image(link, width=300)

                    if(st.button('TEAM RIGHT')):
                        st.session_state.action+=1
                    st.text("")
      
        

        if choose=='MEMES':
    
                # DRAMA
            list1 = [
                     "https://cdn.broadbandsearch.net/images/blogs/most-popular-internet-memes-in-history/scumbag-steve.jpg",
                     "https://sweatpantsandcoffee.com/wp-content/uploads/2018/12/1-Shampoo-in-eye-guide-dog-meme-600x466.jpg",
                     "https://preview.redd.it/ffnpor4qbjm61.jpg?width=640&crop=smart&auto=webp&s=38d70d75c05f1a0edb9be79864e1ca58f654f8cc",
                     "http://pm1.narvii.com/7412/26ff708a6494a1438bf006cf288b37cd65015b8ar1-750-995v2_uhq.jpg",
                     "https://techcommunity.microsoft.com/t5/image/serverpage/image-id/364840iE5DAE8BCD2C08C10/image-size/medium?v=v2&px=400",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtPYh-zD4PvuitdKzOtYdjqQ17i-12OyDR5g&usqp=CAU",
                     "https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/8/asset/buzzfeed-prod-fastlane-02/sub-buzz-2780-1501675431-8.png?output-quality=auto&output-format=auto&downsize=640:*",
                     ]
            # COMEDY
            list2 = ["https://i.pinimg.com/originals/c6/21/72/c62172c5234602861377c1c08e2b4d9e.gif",
                     "https://www.memesmonkey.com/images/memesmonkey/38/38e21fc0ab8abc30bd1a5127ce5b8e01.jpeg",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC57mSGog_BZBBGYK9mYo4mjbNb1np8gkCiA&usqp=CAU",
                     "https://www.liveabout.com/thmb/BDyW8dxHU9sFwsWex4IBwTBk_gQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/3bjzqd-316ae73412af4d76b43b8cccc4a97ba5.jpg",
                     "https://i.pinimg.com/736x/84/93/24/8493249ebd7168416a39143f0f9f4e45.jpg",
                     "https://filmdaily.co/wp-content/uploads/2021/04/bestfriends_lede.jpg",
                     "https://www.liveabout.com/thmb/Zgk_8zg-PYzx1Tb5U-RZYPZMxtQ=/750x670/filters:no_upscale():max_bytes(150000):strip_icc()/AvengersMemes19-b290903f8d8a47118f3ef98f4dcd8bb7.jpg",
                     "https://static.wikia.nocookie.net/1e371388-62a7-48dc-8d95-e46dc16c8c8e",
                     "https://i.pinimg.com/736x/57/57/fa/5757fa53a5ef09ed0acbd8d2f06d7a30.jpg"]

            st.markdown(""" <style> .question_font {color: green} </style> """, unsafe_allow_html=True)


            st.markdown('<h1 class="question_font">YOU LAUGH, YOU LOSE</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with st.container():
                with col1:
                    link = random.choice(list1)
                    st.image(link, width=300)
                    if(st.button('HAHAHA')):
                        st.session_state.comedy += 1
                with col2:
                    link = random.choice(list2)
                    st.image(link, width=300)
                    if(st.button('HEHEHE')):
                        st.session_state.drama += 1

                my_expander = st.expander(label='Result')
           


       
    
        elif choose == "RESULTS":
            st.markdown(""" <style> .question_font {
            font-size:24px ; font-family: 'Clarendon'; border-radius: 5px; padding:10px; text-align: center; color: #FF9633; background-colour: pink} 
            </style> """, unsafe_allow_html=True)
            #STYLE
            st.markdown(""" <style> h3 {
             text-align: center; } </style> """, unsafe_allow_html=True)
            st.markdown(""" <style> img {
             width: 300px; height: 300px } </style> """, unsafe_allow_html=True)
            st.markdown('<h1 class="question_font">RESULT TIME!</p>', unsafe_allow_html=True)
            sort_results = [st.session_state.thriller,st.session_state.animation, st.session_state.romance, st.session_state.family, 
                            st.session_state.scifiction, st.session_state.action, st.session_state.drama, st.session_state.comedy]
            my_dict = {"THRILLER": st.session_state.thriller, "ANIMATION": st.session_state.animation, "ROMANCE": st.session_state.romance, 
                       "FAMILY": st.session_state.family,"SCIFICTION": st.session_state.scifiction, "ACTION": st.session_state.action,
                       "DRAMA": st.session_state.drama,"COMEDY": st.session_state.comedy}
            sorted_dict_items = sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True)
            sort_results.sort()
            i=0
            top_genre_list=[]
            while i<3:
                x=sorted_dict_items[i][0]
                top_genre_list.append(x)
                i+=1
            print("hsuhdjo")
            poster_link=""
            movie_name=""
            #dict1 = {"punjabi chiken":"data:image/jpeg;base64,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","mutton rogan josh":"data:image/jpeg;base64,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","Butter Chicken":"https://images.immediate.co.uk/production/volatile/sites/30/2021/02/butter-chicken-ac2ff98.jpg","Tandoori Chicken":"https://www.foodandwine.com/thmb/3Ng4S6sH9MQEj5Ho1cBkGw2alJ4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/grilled-tandoori-chicken-FT-RECIPE1021-a61b1a767cb74c3c976c85799a378968.jpg","Palak Paneer":"https://images.hindustantimes.com/img/2021/11/26/1600x900/palak_paneer_thumb_1637919968696_1637919979983.jpg","Chole Bhature":"https://i.ytimg.com/vi/csfIOfMnRGg/maxresdefault.jpg","Biryani":"https://c.ndtvimg.com/2022-04/fq5cs53_biryani-doubletree-by-hilton_625x300_12_April_22.jpg"}
            dict1 = {"Gulab Jamun":"https://www.vegrecipesofindia.com/wp-content/uploads/2014/08/gulab-jamun-with-khoya-recipe.jpg","Rasgulla":"https://www.vegrecipesofindia.com/wp-content/uploads/2021/10/rasgulla-recipe-1.jpg","Jalebi":"https://www.vegrecipesofindia.com/wp-content/uploads/2021/11/jalebi-recipe-1.jpg","Kheer":"https://www.vegrecipesofindia.com/wp-content/uploads/2013/10/rice-kheer-2.jpg","Barfi":"https://www.vegrecipesofindia.com/wp-content/uploads/2014/10/barfi-recipe.jpg","Kulfi":"https://www.funfoodfrolic.com/wp-content/uploads/2020/05/Kesar-Pista-Kulfi.jpg","Rabri":"https://www.archanaskitchen.com/images/archanaskitchen/Indian_Sweets_Mithai/Kesar_Pineapple_Rabri_Basundi_Sweet_Mithai_Recipe_Pudding-1.jpg"}

            poster_link1=""
            movie_name1=""
            #dict2 = {"Poronkäristys":"https://images.cdn.soppa365.fi/9f6fbyMfdTjRAoVxe_2_HyZexL8=/1230x0/smart/soppa365.fi/s3fs-public/recipe_main_media/poronkaristys.jpg?itok=t25n4b0C","Riistakäristys":"data:image/jpeg;base64,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","Hernekeitto":"https://www.myllynparas.fi/sites/default/files/images/Hernekeittonettikuva.jpg","Karjalanpaisti":"https://images.cdn.soppa365.fi/iQg2SEGYO7iKKn15aska9uvwT-g=/1230x0/smart/soppa365.fi/s3fs-public/recipe_main_media/karjalanpaisti.jpg?itok=MXmL4CN0","lohikeitto":"https://must-love-garlic.com/wp-content/uploads/2022/01/1-20.jpg","Makkarakeitto":"https://images.cdn.soppa365.fi/WkPh9eu_NJVbLXRJsbjv0uVgcHk=/1230x0/smart/soppa365.fi/s3fs-public/recipe_main_media/linssi-makkarakeitto_1.jpg?itok=xepFvYl1&timestamp=1598957577"}
            dict2 = {"Pulla":"https://www.allrecipes.com/thmb/J9-uC6faxMZaNfViIAck2zKpxiQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8008-fa9f093bf5c54d7ebf102876ae2294dd.jpg","Runeberg's Torte":"https://en.wikipedia.org/wiki/File:Runebergintorttu.jpg","Mustikkapiirakka":"https://www.beyondkimchee.com/wp-content/uploads/2022/06/Finnish-Blueberry-Pie-10.jpg","Lihapiirakka":"https://www.bautrip.com/images/food/lihapiirakka-finland.jpg","Vispipuuro":"https://img.sndimg.com/food/image/upload/f_auto,c_thumb,q_55,w_860,ar_3:2/v1/img/recipes/45/73/81/pic8x6cGM.jpg","Mämmi":"https://images.cdn.yle.fi/image/upload/w_1200,h_675,ar_1.7777777910232544,dpr_1,c_fill,g_faces/q_auto:eco,f_auto,fl_lossy/13-3-7905511","Pannukakku":"https://www.allrecipes.com/thmb/ANvf1NV-JvB-84eZp02FtGvIbDA=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/9422601-dffac077b10b4a68a024d9d612d204de.jpg","Korvapuusti":"https://www.google.com/search?q=korvapuusti&rlz=1C1RXQR_enIN966IN966&sxsrf=APwXEdcW90EN-T9mcXM-MKqg9yXvAHHQvw:1682009626813&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiKk8KS9rj-AhUw-TgGHULJBBgQ_AUoAXoECAEQAw&biw=1536&bih=722&dpr=1.25#imgrc=-uyLOs_8opMduM"}
            #FUNCTION TO RECOMMEND MOVIES BASED ON USER REPLIES
            # def get_movies(top_genre_list):
            #     maxi=0
            #     #sum_score=0
            #     for id in quiz.index:  
            #         sum_score=0
            #         for genre in top_genre_list:
            #             sum_score+= quiz[genre][id]
            #             if(sum_score>maxi):
            #                 maxi=sum_score
            #                 poster_link=quiz['LINK'][id]
            #                 movie_name=quiz['NAME'][id]
            #     return poster_link, movie_name
            #poster_link, movie_name= get_movies(top_genre_list)
            key, val = random.choice(list(dict1.items()))
            movie_name = key
            poster_link = val 
            #########################
            key1, val1 = random.choice(list(dict2.items()))
            movie_name1 = key1
            poster_link1 = val1 
            with st.container():
                col1, col2= st.columns([0.2, 0.2])
                col2.image(poster_link,use_column_width=True)
                col2.subheader(movie_name)
                col1.image(poster_link1,use_column_width=True)
                col1.subheader(movie_name1) 
                # with st.expander("PLAY THE TRAILER"):
                #     yt_link = play_yt_video(movie_name)
                #     st.video(yt_link)
        #profile_data(poster_link,1)
        with st.expander("Disclaimer"):
            st.write("The recommendation is just for fun and doesn't mean to hurt your sentiments in any manner.")
            st.write(" ")
            st.write("The food item suggested may or may not be vegetarian. It may also contain ingredients that you will be allergic to. Please check the ingredients. We are working on a version that will be able to cater to different needs.")
            
        
                
            
            
            
            
    elif choose == 'Map':
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633; text-align:center;} 
        </style> """, unsafe_allow_html=True)
        
        
        st.markdown('<h1 class="font">INDIAN MAP</p>', unsafe_allow_html=True)
        
    
        st.write('Click upon different states to get regional movie recommendations.')
        
        #FUNCTION TO MAKE CLICKABLE STATES IN INDIAN MAP USING HTML IMAGE MAPS TAG
        def indian_map():
            return """
            <img src="https://nriol.com/images/india_state_map.png" alt="Workplace" usemap="#workmap">

            <map name="workmap">
              <area shape="poly" coords="236,151,252,157,264,174,259,183,256,193,252,199,237,197,229,199,
              225,187,218,180,210,178,207,166,206,158,210,152,230,146"
              alt="Uttarakhand"  href="https://timesofindia.indiatimes.com/etmoviedetaillisting/61182603.cms">
              
              <area shape="poly" coords="204,570,220,569,233,564,247,561,254,551,259,566,253,584,250,602,
              251,622,235,633,229,653,210,665,192,680,192,635,184,619,175,604" 
              alt="Tamil Nadu" href="https://www.imdb.com/india/top-rated-tamil-movies/">
              
              <area shape="poly" coords="69,294,84,295,101,303,115,321,125,330,126,342,123,353,118,365,116,
              374,118,387,106,390,98,393,82,363,76,375,66,381,50,381,34,369,20,350,25,333,13,320,11,309,14,304"
              alt="Gujarat" href="https://www.imdb.com/list/ls020229870/">
              
              <area shape="poly" coords="270,369,288,349,296,333,289,317,302,310,320,313,331,318,339,331,341,
              345,331,359,318,378,308,399,299,412,299,429,285,445,278,456,268,438,261,424" 
              alt="Chattisgarh" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=hne">
              
              <area shape="poly" coords="36,231.00000762939453,54,217.00000762939453,86,219.00000762939453,108,
              190.00000762939453,121,173.00000762939453,140,191.00000762939453,157,209.00000762939453,167,
              221.00000762939453,186,222.00000762939453,188,261.00000762939453,184,295.00000762939453,164,
              307.00000762939453,140,305.00000762939453,120,327.00000762939453,78,296.00000762939453,58,284.00000762939453,44,261.00000762939453" 
              alt="Rajasthan" href="https://en.wikipedia.org/wiki/List_of_Rajasthani-language_films">
              
              <area shape="poly" coords="134,572.0000076293945,148,593.0000076293945,159,619.0000076293945,
              172,641.0000076293945,176,663.0000076293945,191,673.0000076293945,195,650.0000076293945,188,
              629.0000076293945,167,600.0000076293945,156,588.0000076293945" 
              alt="Kerala" href="https://www.imdb.com/india/top-rated-malayalam-movies/">
              
              <area shape="poly" coords="147,475,165,465,180,454,197,442,197,457,196,481,189,500,182,522,188
              ,538,204,546,218,555,202,572,196,591,176,599,162,591,143,574,132,557,128,535,123,510,130,481" 
              alt="Karnataka" href="https://www.imdb.com/list/ls041049290/">
              
              <area shape="poly" coords="216,490,233,482,247,474,268,465,300,449,316,439,336,427,350,430,336,
              445,306,469,286,486,268,502,254,517,258,535,260,551,248,553,228,563,218,556,200,545,195,531,178,519,194,498"
              alt="Andhra Pradesh" href="https://www.imdb.com/india/top-rated-telugu-movies/">
              
              <area shape="poly" coords="128,489.00001525878906,142,474.00001525878906,158,463.00001525878906,183,453.00001525878906,197,440.00001525878906,
              208,423.00001525878906,222,413.00001525878906,244,417.00001525878906,262,423.00001525878906,266,403.00001525878906,262,383.00001525878906,254,
              370.00001525878906,224,370.00001525878906,196,371.00001525878906,178,373.00001525878906,155,371.00001525878906,130,360.00001525878906,122,
              374.00001525878906,116,389.00001525878906,98,402.00001525878906,92,412.00001525878906,93,435.00001525878906,97,463.00001525878906,106,495.00001525878906" 
              alt="Maharastra" href="https://www.imdb.com/list/ls052798925/">
              
              <area shape="poly" coords="332,231.00001525878906,352,240.00001525878906,378,247.00001525878906,408,
              253.00001525878906,418,274.00001525878906,414,284.00001525878906,396,295.00001525878906,370,295.00001525878906,
              355,304.00001525878906,337,303.00001525878906,325,281.00001525878906" 
              alt="Bihar" href="https://www.imdb.com/list/ls090204907/">
              
              <area shape="poly" coords="128,175.00000190734863,132,157.00000190734863,147,149.00000190734863,144,134.00000190734863,162,125.00000190734863,166,
              135.00000190734863,174,141.00000190734863,183,151.00000190734863,183,163.00000190734863,172,175.00000190734863,162,179.00000190734863" 
              alt="Punjab" href="https://www.imdb.com/list/ls066141330/">
              
              <area shape="poly" coords="167,217.00001525878906,158,209.00001525878906,149,190.00001525878906,133,181.00001525878906,162,181.00001525878906,178
              ,170.00001525878906,197,173.00001525878906,194,205.00001525878906,198,218.00001525878906,193,228.00001525878906"
              alt="Haryana" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=bgc">
              
              <area shape="poly" coords="468,259,482,257,506,254,518,260,514,271,473,273,461,271" 
              alt="Meghalaya" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=kha">
              
              <area shape="poly" coords="462,260,458,252,460,241,476,241,489,239,506,237,530,227,544,217,554,209,576,199,582,210,560,226,
              549,237,545,248,537,254" alt="Assam" href="https://www.imdb.com/list/ls093032155/">
              
              <area shape="poly" coords="526,288.00000190734863,533,276.00000190734863,536,269.00000190734863,540,261.00000190734863,553,259.00000190734863,
              561,257.00000190734863,562,267.00000190734863,562,277.00000190734863,559,283.00000190734863,555,292.00000190734863,545,293.00000190734863,538,295.00000190734863" 
              alt="Manipur" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=mni">
              
              <area shape="poly" coords="435,359,444,358,449,354,448,345,446,337,445,324,439,315,436,307,427,296,427,286,432,279,436,274,
              429,265,428,256,441,252,449,253,448,241,434,234,423,234,418,261,417,276,417,300,412,306,406,310,397,312,390,317,383,321,378,323,399,341,405,350,414,359" 
              alt="West Bengal" href="https://www.imdb.com/list/ls021587889/">
              
              <area shape="poly" coords="4286,450,290,442,299,429,303,419,299,407,308,406,312,400,308,392,309,381,318,376,326,373,329,366,
              331,351,340,348,352,347,367,352,383,352,387,345,398,350,412,360,404,374,401,388,395,395,371,404,366,412,354,424,333,425"
              alt="Odisha" href="https://www.imdb.com/search/title/?languages=or&sort=user_rating">
              
              <area shape="poly" coords="199,492,194,486,197,477,195,468,199,462,199,452,200,442,201,436,205,431,204,425,209,422,216,
              418,218,408,228,415,236,414,246,415,249,422,257,433,267,437,273,448,279,455,272,462,224,488"
              alt="Telangana" href="https://www.imdb.com/india/top-rated-telugu-movies/">
              
              <area shape="poly" coords="110,500,112,509,116,517,122,518,123,513,124,507,121,503"
              alt="Goa" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=kok">
             
            </map>
            """
        st.markdown(indian_map(), unsafe_allow_html=True)
            
        
        
        
        
        
        
    elif choose == 'Profile':
        
        st.markdown(""" <style> .result_font {
            font-size:40px ; font-family: 'Cooper Black'; text-align: center; color: #FF9633; background-colour: pink} 
            </style> """, unsafe_allow_html=True)
            
        st.markdown('<h1 class="result_font">RESULT TIME!</p>', unsafe_allow_html=True)
            
        #STYLE
        st.markdown(""" <style> h3 {
         text-align: center; } </style> """, unsafe_allow_html=True)
            
        st.markdown(""" <style> img {
         width: 300px; height: 300px; border-radius:10px; border: 10px solid lightgray;
         } </style> """, unsafe_allow_html=True)
        
        
            
        st.subheader("YOUR TOP MOVIE RECOMMENDATION RESULTS:")
        if(len(st.session_state.profile_content_recommendations)==0):
            st.warning("SEARCH SOME MOVIES IN CONTENT RECOMMENDATION SECTION TO CONTINUE")
            
        else:
            key=0
            while key<len(st.session_state.profile_content_recommendations):
                with st.container():
                    col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                    col2.image(st.session_state.profile_content_recommendations[key]["link"],use_column_width=True)
                key+=1
                
                
        st.subheader("YOUR TOP BUZZFEED MOVIE RECOMMENDATION RESULTS:")
        if(len(st.session_state.profile_buzzfeed_recommendations)==0):
           st.error("ATTEMP SOME QUESTIONS IN THE BUZZFEED SECTION TO CONTINUE")
       
        
        else:
           key=0
           while key<len(st.session_state.profile_buzzfeed_recommendations):
               with st.container():
                   col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                   col2.image(st.session_state.profile_buzzfeed_recommendations[key]["link"],use_column_width=True)
               key+=1
                
        

if __name__ == '__main__':
    main()
