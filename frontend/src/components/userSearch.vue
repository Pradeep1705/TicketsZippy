<template>
  <div class="venue-shows-container">
    <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
      <b-navbar-brand class="navbar-logo">Your Venue</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item  class="nav-item"><router-link to="/home">Home</router-link></b-nav-item>
          <b-nav-item  class="nav-item"><router-link to="/userProfile">Profile</router-link></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          

          <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <br>
    <b-row class="text-center" v-if="venues.length > 0">
      <b-col md="12">
        <h3>venues related to your search:</h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col v-for="venue in venues" :key="venue.ID" md="4" class="show-card">
        <b-card
          :title="venue.name"
          tag="article"
          class="show-card-inner"
        >
        <div class="venue-image-container">
          <img :src="getImageSrc(venue.img)" alt="Venue Image" class="venue-image" />
        </div>
          
          <b-card-text class="show-card-text">
            Some quick example text to build on the card title and make up the bulk of the card's content.
          </b-card-text>

          <b-button variant="primary" class="view-shows-btn">
            <router-link :to="`/shows/${venue.ID}`">View Shows</router-link>
          </b-button>
        </b-card>
      </b-col>
    </b-row>


    <b-row class="text-center" v-if="places.length > 0" >
      <b-col md="12">
        <h3>venues related to your place:</h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col v-for="venue in places" :key="venue.ID" md="4" class="show-card">
        <b-card
          :title="venue.name"
          tag="article"
          class="show-card-inner"
        >
        <div class="venue-image-container">
          <img :src="getImageSrc(venue.img)" alt="Venue Image" class="venue-image" />
        </div>
          
          
          <b-card-text class="venue-card-text">
            Place: {{venue.place}}
          </b-card-text>

          <b-button variant="primary" class="book-tickets-btn">
            <router-link to="/userShow">View Shows</router-link>
          </b-button>
        </b-card>
      </b-col>
    </b-row>

    <b-row class="text-center" v-if="shows.length > 0" >
      <b-col md="12">
        <h3>shows  related to your search:</h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col v-for="show in shows" :key="show.ID" md="4" class="show-card">
        <b-card
          :title="show.name"
          tag="article"
          class="show-card-inner"
        >
        <div class="venue-image-container">
          <img :src="getImageSrc(show.img)" alt="Venue Image" class="venue-image" />
        </div>
          
          <b-card-text class="venue-card-text">
           Venue Name: {{ show.venueName }}
           Ticket price: {{show.ticket}}
          </b-card-text>

          <b-button variant="primary" class="book-tickets-btn">
            <router-link :to="`/bookTicket/${show.ID}/${show.venueID}`">Book Tickets</router-link>
          </b-button>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';


export default{
   
      data() {
        return {
          venues: [],
          shows: [],
          places: [],
          
        };
      },
      mounted() {
        this.getSearched();
      },
      methods: {
        getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
        getSearched() {
            console.log(this.$route)
            const searchData = this.$route.params.keyword;
            let payload = {'searched': searchData}
            axios.post('http://127.0.0.1:5000/search', payload,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.venues=response.data.venues;
                this.shows=response.data.shows;
                this.places=response.data.places;
            })
          .catch(error=> console.error('error :',error));
        },
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      }
        
       
      
        
      }
    
}
</script>


<style scoped>
/* General styles */
.venue-shows-container {
  padding: 0px;
  background-image: url("@/assets/gradient.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.view-shows-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #007bff;
}

.view-shows-btn a {
  color: white;
  text-decoration: none;
}

.show-card {
  margin-bottom: 20px;
}

.venue-image-container {
  width: 100%; 
  height: 200px; 
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.venue-image {
  max-width: 100%;
  max-height: 100%;
}

.gradient-nav {
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.3)), url("@/assets/blue.jpeg");
  background-size: cover;
  background-position: center;
  color: white;
}

.venue-card-text {
  font-size: 18px;
  color: #ffffff;
}

.navbar-logo {
  font-size: 24px;
  font-weight: bold;
}

.nav-item {
  font-size: 16px;
}

.nav-item a{
  color: white;
  text-decoration: none;
}

/* Search bar styles */
.search-form {
  margin-bottom: 10px;
}

.search-input {
  border-radius: 20px;
  border: none;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 8px 12px;
  color: #333;
}

.search-button {
  border-radius: 20px;
  margin-left: 10px;
  background-color: #007bff;
  color: white;
  font-weight: bold;
}

/* Login button styles */
.login-button {
  border-radius: 20px;
  background-color: #f55;
  color: white;
  font-weight: bold;
}

.login-button a {
  color: white;
  text-decoration: none;
}

/* Show card styles */
.show-card-inner {
  border: none;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
  background-image: url("@/assets/blue.jpeg");
  background-size: cover;
  background-position: center;
}

.show-card-text {
  font-size: 14px;
  color: #555;
}

.book-tickets-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #007bff;
}

.book-tickets-btn a {
  color: white;
  text-decoration: none;
}

/* Media queries for responsiveness */
@media screen and (max-width: 767px) {
  .show-card {
    flex: 0 0 100%;
    max-width: 100%;
  }
}
</style>