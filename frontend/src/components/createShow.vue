<template>
  <div class="create-venue-container">
    <h1>Create Show</h1>
    <form @submit.prevent="submitForm" class="venue-form">
      <!-- Show Name -->
      <label for="name">Show Name:</label>
      <input type="text" id="name" v-model="name" required />

      <!-- Show Tags -->
      <label for="tags">Tags:</label>
      <input type="text" id="tags" v-model="tags" required />

      <!-- Show date  -->
      <label for="date">Date:</label>
      <input type="date" id="date" v-model="date" required />

      <!-- Show Ticket -->
      <label for="ticket">Ticket Price:</label>
      <input type="number" id="ticket" v-model="ticket" required />
      
      
      <!-- Show Rating -->
      <label for="rating">Rating:</label>
      <input type="number" id="rating" v-model="rating" required />

      <!-- Show Image -->
      <label for="upload_image">Image:</label>
      <input type="file" id="upload_image" name="upload_image" @change="handleImageUpload" required />

      <button type="submit" class="submit-button">Submit</button>
    </form>

    <!-- Display the created show -->
    <div v-if="createdShow">
      <h2>Created Show:</h2>
      <p>Name: {{ createdShow.name }}</p>
      <p>Tags: {{ createdShow.tags }}</p>
      <p>Date: {{ createdShow.date }}</p>
      <p>Price: {{ createdShow.ticket }}</p>
      <p>Rating: {{ createdShow.rating }}</p>
      <div class="venue-image-container">
        <img :src="getImageSrc(createdShow.img)" class="venue.image" alt="Venue Image"/>
      </div>
      <b-button type="button" variant="secondary" class="go-back-button">
        <router-link to="/adminVenue">Go back</router-link>
      </b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      tags: '',
      date: '',
      ticket: '',
      rating: '',
      uploadImage: null,
      createdShow: null,
    };
  },
  methods: {
     getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
    handleImageUpload(event) {
      this.uploadImage = event.target.files[0];
    },
    getImageUrl(imageName) {
      return `${imageName}`;
    },
    submitForm() {
      const formData = new FormData();
      formData.append('name', this.name);
      formData.append('tags', this.tags);
      formData.append('date', this.date);
      formData.append('ticket', this.ticket);
      formData.append('rating', this.rating);
      formData.append('upload_image', this.uploadImage);

      const venueID = this.$route.params.venueID;
      const apiurl = `http://127.0.0.1:5000/createShow/${venueID}/` 

      axios
        .post(apiurl, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
             Authorization: localStorage.getItem('token')
          },
        })
        .then((response) => {
          this.createdShow = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.create-venue-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.venue-form {
  margin-top: 20px;
}

.venue-form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.venue-form input[type="text"],
.venue-form input[type="number"],
.venue-form input[type="file"] {
  width: 100%;
  padding: 8px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.created-venue {
  margin-top: 30px;
  text-align: center;
}

.venue-details {
  margin-bottom: 15px;
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

.go-back-button {
  margin-top: 20px;
}
</style>
