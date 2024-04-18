<template>
  <div class="venues-container">
    <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo">Tickets Zippy</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item class="nav-item"><router-link to="/userProfile">Profile</router-link></b-nav-item>
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
      <b-col v-for="venue in venues" :key="venue.ID" md="4" class="venue-card">
        <b-card
          :title="venue.name"
          :title-tag="'h3'"
          class="venue-card-inner"
          tag="article"
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

          <b-button variant="primary" class="view-shows-btn">
            <router-link :to="`/shows/${venue.ID}`">View Shows</router-link>
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
      form: {
        searchQuery: ''
      }
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
        .get('http://127.0.0.1:5000/getVenues',{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
        .then((response) => {
          this.venues = response.data;
           
        })
        .catch((error) => console.error('error:', error));
        
    },
    onSubmit(event) {
        event.preventDefault()
        let url = `/search/${this.form.searchQuery}`;
        console.log(url)
        console.log(this.form.searchQuery)
        // console.log(payload)
        this.$router.push(url);
       
      },
      ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      }
    
  }
};
</script>

<style scoped>
/* General styles */
.venues-container {
  padding: 0px;
  background-image: url("@/assets/gradient.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.venue-card {
  margin-bottom: 20px;
  padding: 0 50px 0 50px;
}

.b-card-title {
  font-weight: bold;
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

.nav-item a{
  color: white;
  text-decoration: none;
}

.gradient-nav {
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.3)), url("@/assets/blue.jpeg");
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


.venue-card-inner {
  border: none;
  border-radius: 10px;
  box-shadow: 0px 8px 16px rgb(0, 0, 0);
  background-image: url("@/assets/blue.jpeg");
  background-size: cover;
  font-weight: bold;
  background-position: center;
}

.venue-card-text {
  font-size: 18px;
  color: #ffffff;
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


@media screen and (max-width: 767px) {
  .venue-card {
    flex: 0 0 100%;
    max-width: 100%;
  }
}
</style>