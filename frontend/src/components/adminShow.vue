<template>
  <div class="venue-shows-container">
    <b-navbar toggleable="lg" type="danger" variant="info" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo">Your Venue</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/adminVenue" class="nav-item">Home</b-nav-item>
          
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          

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

          <b-button variant="primary" class="view-shows-btn">
            <router-link :to="`/editShow/${show.ID}/${show.venueID}`">Edit Show</router-link>
          </b-button>
          <b-button  variant="danger" @click="showDeleteConfirmation(show)" style="margin-top: 10px;">Delete Show</b-button>
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
          shows: []
        };
      },
      created() {
        this.getShows();
      },
      methods: {
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      },
        getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
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
        showDeleteConfirmation(show) {
      const confirmDelete = window.confirm(`Do you want to delete '${show.name}'?`);
      if (confirmDelete) {
        this.deleteShow(show);
      }
    },
    deleteShow(show) {
      const showID = show.ID;
      const apiurl = `http://127.0.0.1:5000/deleteShow/${showID}/`;

      axios
        .post(apiurl)
        .then(() => {
          this.getShows();
        })
        .catch((error) => {
          console.error(error);
          // Handle error, e.g., show an error message
        });
    },
      },
      
    
}
</script>

<style scoped>
/* General styles */
.venue-shows-container {
  padding: 0px;
  background-image: url("@/assets/dark.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.view-shows-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #2a2f356b;
  border: black;
}

.venue-card-text {
  font-size: 18px;
  color: #000000;
}

.view-shows-btn a {
  color: white;
  text-decoration: none;
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

.show-card {
  margin-bottom: 20px;
  padding: 0 50px 0 50px;
}

.gradient-nav {
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.3)), url("@/assets/card.jpeg");
  background-size: cover;
  background-position: center;
  color: white;
}

.navbar-logo {
  font-size: 24px;
  font-weight: bold;
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
  background-image: url("@/assets/card.jpeg");
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