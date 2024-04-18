<template>
  <div class="book-ticket-container">
    <b-navbar toggleable="lg" type="danger" variant="info" class="gradient-nav">
      <b-navbar-brand href="#" class="navbar-logo">Your Venue</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item  class="nav-item"><router-link to="/home">Home</router-link></b-nav-item>
          <b-nav-item  class="nav-item"><router-link to="/userProfile">Profile</router-link></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-button variant="secondary" class="login-button" size="sm"  @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <h2 class="book-ticket-heading">Book Your Tickets</h2>

    <b-form @submit="onSubmit" class="ticket-form">
      <div class="show-details">
        <h2>{{ show_data.name }}</h2>

        <b-form-group id="input-group-2" label="No. of seats:" label-for="input-2">
          <b-form-input id="input-2" v-model="seats" placeholder="Enter here..." required></b-form-input>
        </b-form-group>
      </div>

      <b-button type="submit" variant="primary" class="book-tickets-btn" >Submit</b-button>
      
    
  
    </b-form>
  </div>
</template>





<script>

import axios from 'axios'

import { mapActions } from 'vuex'



export default {
   
    data() {
      return {
        modalVisible: false,
        show_data:{},
        seats: ''
      }
    },
    mounted(){
        this.getDetails();
    },
    
    methods: {
      

      onSubmit(event) {
        event.preventDefault()
        const showID = this.$route.params.showID;
        const venueID = this.$route.params.venueID;
        let payload = {"ticket":this.seats}
        console.log(payload)
        const apiurl=`http://127.0.0.1:5000/bookTicket/${showID}/${venueID}/`
        axios.post(apiurl,payload,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
            username: localStorage.getItem('username')
        })
        
            .then((res)=>{
                console.log('response tag')
                if(res.data.message==='tickets_excess'){
                    alert('Request no.of.tickets not available');
                    return
                }
                else{             
                    console.log('else tag')
                    alert('Tickets Booked Sucessfully')
                    this.$router.push('/userProfile')
                }
            })
       
      },
      
      ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      },
      
      getDetails(){
        const showID = this.$route.params.showID;
        const venueID = this.$route.params.venueID;
        const apiurl=`http://127.0.0.1:5000/bookTicket/${showID}/${venueID}/`
        axios.get(apiurl,{
            headers: {
                Authorization:localStorage.getItem('token')
            },
            username: localStorage.getItem('username')
        })
            .then(response=> {
                this.show_data=response.data;
                if (response.data.message === "tickets_unavailable"){
                  alert('Houseful')
                  this.$router.push(`/shows/${venueID}`)
                }
            })
          .catch(error=> console.error('error :',error)); 
      },
      
    }
  }



</script>

<style scoped>
/* General styles */
.book-ticket-container {
  padding: 0px;
  background-image: url("@/assets/gradient.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

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

.book-ticket-heading {
  margin-top: 30px;
  font-size: 32px;
  font-weight: bold;
  color: #333;
  text-align: center;
}

/* Ticket form styles */
.ticket-form {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 10px;
}

.nav-item a{
  color: white;
  text-decoration: none;
}

.show-details {
  text-align: center;
  margin-bottom: 20px;
}

.show-details h2 {
  font-size: 24px;
  font-weight: bold;
}

/* Book tickets button styles */
.book-tickets-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #007bff;
  font-size: 18px;
  font-weight: bold;
}

.book-tickets-btn a {
  color: white;
  text-decoration: none;
}

/* Media queries for responsiveness */
@media screen and (max-width: 767px) {
  .ticket-form {
    width: 90%;
  }
}
</style>