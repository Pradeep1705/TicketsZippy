<template>
  <div class="venues-container">
    <b-navbar toggleable="lg" type="light" variant="light" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo">Your Venue</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          

          <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
      <br>
      <b-button variant="primary" class="view-shows-btn">
            <router-link to="/createVenue ">Create Venue</router-link>
      </b-button>
          
    <b-row>
      
      <b-col v-for="venue in venues" :key="venue.ID" md="4" class="venue-card">
        <b-card
          :title="venue.name"
          tag="article"
          class="venue-card-inner"
        >
        <div class="venue-image-container">
          <img :src="getImageSrc(venue.img)" alt="Venue Image" class="venue-image" />
        </div>
          
          
          <b-card-text class="venue-card-text">
            Place:  {{ venue.place }}
          </b-card-text>
          <b-card-text class="venue-card-text">
            Capacity:  {{ venue.capacity }}
          </b-card-text>
          <b-card-text class="venue-card-text">
            Ratings:  {{ venue.rating }}
          </b-card-text>
        <div class="button-row">
          <b-button variant="secondary" class="view-shows-btn" style="margin-right: 10px;">
            <router-link :to="`/adminShow/${venue.ID}`">View Shows</router-link>
          </b-button>
          <b-button variant="primary" class="view-shows-btn">
            <router-link :to="`/createShow/${venue.ID}`">Create shows</router-link>
          </b-button>
        </div>
        <div class="button-row">
          <b-button variant="primary" class="view-shows-btn" style="margin-right: 10px;">
            <router-link :to="`/editVenue/${venue.ID}`">Edit Venue</router-link>
          </b-button>
          <b-button variant="primary" class="view-shows-btn">
            <router-link :to="`/exportPage/${venue.ID}`">Venue dashboard</router-link>
          </b-button>
        </div>
            <b-button type="button" variant="danger" @click="showDeleteConfirmation(venue)" style="margin-top: 10px;">
                Delete Venue
            </b-button>
         
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>


<script>
import axios from 'axios';
import {mapActions} from 'vuex'
export default {
    
  data() {
    return {
      venues: [],
      
    };
  },
  mounted() {
    this.getVenues();
  },
  methods: {
    getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
    getVenues() {
      axios
        .get('http://127.0.0.1:5000/adminVenues',{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
        .then((response) => {
          this.venues = response.data;
          // if(response.data.message==='Token is missing'){
          //   alert('Token is Missing');
          // }
        })
        .catch((error) => console.error('error :', error));
    },
    
    showDeleteConfirmation(venue) {
      const confirmDelete = window.confirm(`Do you want to delete '${venue.name}'?`);
      if (confirmDelete) {
        this.deleteVenue(venue);
      }
    },
    ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      },
    
    deleteVenue(venue) {
      const venueID = venue.ID;
      const apiurl = `http://127.0.0.1:5000/deleteVenue/${venueID}/`;

      axios
        .post(apiurl)
        .then(() => {
          this.getVenues();
        })
        .catch((error) => {
          console.error(error);
          // Handle error, e.g., show an error message
        });
    },
  },
};
</script>

<style scoped>
/* General styles */
.venues-container {
  padding: 0px;
  background-image: url("@/assets/dark.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.venue-card-text {
  font-size: 18px;
  color: #000000;
}

.venue-card {
  padding: 0 50px 0 50px;
  margin-bottom: 20px;
}

.button-row {
  display: flex;
  justify-content: space-between;
  /* align-items: center; */
  margin-top: 10px;
  
  
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
  background-image: linear-gradient(to right, rgba(255, 255, 255, 0.7), rgb(0, 0, 0)), url("@/assets/card.jpeg");
  background-size: cover;
  background-position: center;
  color: white;
}

.navbar-logo {
  font-size: 24px;
  font-weight: bold;
  color: white;
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

/* Venue card styles */
.venue-card-inner {
  
  border: none;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
  background-image: url("@/assets/card.jpeg");
  background-size: cover;
  background-position: center;
}




.view-shows-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #2a2f356b;
  border: black;
}

.view-shows-btn a {
  color: white;
  text-decoration: none;
}

.view-shows-btn:last-child {
  margin-right: 0;
}

/* Media queries for responsiveness */
@media screen and (max-width: 767px) {
  .venue-card {
    flex: 0 0 100%;
    max-width: 100%;
  }
}
</style>
