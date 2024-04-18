<template>
  <div class="venues-container">
    <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
      <b-navbar-brand href="#" class="navbar-logo">Tickets Zippy</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#" class="nav-item"><router-link to="/home">home</router-link></b-nav-item>
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

    
    <div class="user-info" >
      <h2>Welcome, {{ userData.username }}</h2>
      
    </div>

    <h2 class="user-tickets-heading">Your Booked Tickets</h2>

    <div class="tickets-list">
      <b-card class="ticket-card" v-for="ticket in ticketList" :key="ticket.ID">
        <div class="ticket-image">
          <img :src="getImageSrc(ticket.img)" alt="Ticket Image" class="image-preview" />
        </div>
        <div class="ticket-details">
        <b-card-title class="ticket-title">{{ ticket.showName }}</b-card-title>
        <b-card-text class="ticket-info">
          <b>Number of Tickets:</b> {{ ticket.seats }}
        </b-card-text>
        <b-card-text class="ticket-info">
          <b>Venue Name:</b> {{ ticket.venueName }}
        </b-card-text>
        <b-card-text class="ticket-info">
          <b>Booking Date:</b> {{ ticket.date }}
        </b-card-text>
        <b-card-text class="ticket-info">
          <b>Price:</b> {{ ticket.price }}
        </b-card-text>
        </div>
      </b-card>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import {mapActions} from 'vuex'



export default {

    data(){
        return{
            userData:[],
            ticketList:[],
            form: {
        searchQuery: ''
      }
        }
    },
    mounted(){
        this.getUser();
    },
    methods: {
      getImageSrc(imageData) {
      return `data:image/png;base64,${imageData}`;
    },
        getUser(){
            axios
        .get('http://127.0.0.1:5000/userProfile',{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
        .then((response) => {
          this.userData = response.data.userData;
          this.ticketList = response.data.ticketList;
           
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
}
</script>

<style scoped>


.search-button {
  border-radius: 20px;
  margin-left: 10px;
  background-color: #007bff;
  color: white;
  font-weight: bold;
}


.login-button {
  border-radius: 20px;
  background-color: #f55;
  color: white;
  font-weight: bold;
}

.nav-item a{
  color: white;
  text-decoration: none;
}

.venues-container {
  padding: 0;
  background-image: url("@/assets/gradient.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
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

.user-info {
  text-align: center;
  margin-bottom: 20px;
}

.user-info h2 {
  font-size: 32px;
  font-weight: bold;
}

.user-tickets-heading {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  text-align: center;
}

/* Ticket card styles */
.tickets-list {
  padding: 0 50px 0 50px;
  display: flex;
  flex-wrap: wrap;
  /* justify-content: space-between; */
  margin: 0 -10px;
}

.ticket-card {
  width: 300px;
  display: flex;
  align-items: center; 
  margin: 15px;
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 15px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.ticket-card:hover {
  transform: translateY(-5px);
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
}
.ticket-image {
  width: 100%; 
  height: 200px; 
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-preview{
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.ticket-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #007bff;
}

.ticket-info {
  font-size: 16px;
  color: #333;
}

.ticket-card b-card-title {
  font-size: 20px;
  font-weight: bold;
}

.ticket-card b-card-text {
  font-size: 16px;
}

.ticket-details {
  flex: 1;
}

/* Media queries for responsiveness */
@media screen and (max-width: 767px) {
  .ticket-card {
    width: 90%;
  }
}
</style>