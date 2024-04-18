<template>
  <div class="venue-shows-container">
    <b-navbar toggleable="lg" type="danger" variant="info" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo">Tickets Zippy</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item  class="nav-item"><router-link to="/home">Home</router-link></b-nav-item>
          <b-nav-item  class="nav-item"><router-link to="/userProfile">Profile</router-link></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form @submit="onSubmit">
            <b-form-input v-model="form.searchQuery" size="sm" class="search-input" placeholder="Search"></b-form-input>
            <b-button size="sm" class="search-button" type="submit">Search</b-button>
          </b-nav-form>

          <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <br>

    <b-row>
      <b-col v-for="show in shows" :key="show.ID" md="4" class="show-card">
        <b-card
          :title="show.name"
          tag="article"
          class="show-card-inner"
        >
        <div class="show-image-container">
          <img :src="getImageSrc(show.img)" alt="Show Image" class="show-image" />
        </div>
          
          
          <b-card-text class="venue-card-text">
            Tags: {{ show.tags }}
          </b-card-text>
          <b-card-text class="venue-card-text">
            Date: {{ show.date }}
          </b-card-text>
          <b-card-text class="venue-card-text">
            Price: Rs.{{ show.ticket }}
          </b-card-text>
          <b-card-text class="venue-card-text">
            Ratings: {{ show.rating }}
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
import axios from 'axios'
import {mapActions} from 'vuex'


export default{
    
      data() {
        return {
          shows: [],
          form: {
            searchQuery: ''
        }
        };
      },
      created() {
        this.getShows();
      },
      methods: {
        getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      },
        getShows() {
            const venueID = this.$route.params.venueID;
            const apiurl = `http://127.0.0.1:5000/getShows/${venueID}/` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.shows=response.data;
            })
          .catch(error=> console.error('error :',error));
        },
        onSubmit(event) {
        event.preventDefault()
        let url = `/search/${this.form.searchQuery}`;
        console.log(url)
        console.log(this.form.searchQuery)
        // console.log(payload)
        this.$router.push(url);
       
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

.show-card {
  margin-bottom: 20px;
}

.venue-card-text {
  font-size: 18px;
  color: #ffffff;
}

.show-image-container {
  width: 100%; 
  height: 200px; 
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.show-image {
  max-width: 100%;
  max-height: 100%;
}

.show-card-text {
  font-size: 20px;
  color: #ffffff;
}

.gradient-nav {
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.3)), url("@/assets/blue.jpeg");
  background-size: cover;
  background-position: center;
  color: rgb(0, 0, 0);
}

.navbar-logo {
  font-size: 24px;
  font-weight: bold;
}

.nav-item a{
  color: white;
  text-decoration: none;
}

.nav-item {
  font-size: 16px;
}

/* Search bar styles */
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