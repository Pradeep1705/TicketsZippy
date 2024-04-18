<template>
  <div class="create-venue-container">
    <h1>Create Venue</h1>
    <form @submit.prevent="submitForm" class="venue-form">
      <!-- Venue Name -->
      <label for="venueName">Venue Name:</label>
      <input type="text" id="venueName" v-model="venueName" required />

      <!-- Venue Place -->
      <label for="place">Place:</label>
      <input type="text" id="place" v-model="place" required />

      <!-- Venue Capacity -->
      <label for="capacity">Capacity:</label>
      <input type="number" id="capacity" v-model="capacity" required />

      <!-- Venue Rating -->
      <label for="rating">Rating:</label>
      <input type="number" id="rating" v-model="rating" required />

      <!-- Venue Image -->
      <label for="upload_image">Image:</label>
      <input type="file" id="upload_image" name="upload_image" @change="handleImageUpload" required />

      <button type="submit"  class="submit-button">Submit</button>
    </form>

    <!-- Display the created venue -->
    <div v-if="createdVenue" class="created-venue">
      <h2>Created Venue:</h2>
      <p><strong>Name:</strong> {{ createdVenue.name }}</p>
      <p><strong>Place:</strong> {{ createdVenue.place }}</p>
      <p><strong>Capacity:</strong> {{ createdVenue.capacity }}</p>
      <p><strong>Rating:</strong> {{ createdVenue.rating }}</p>
      <div class="venue-image-container">
        <img :src="getImageSrc(createdVenue.img)" class="venue-image" alt="Venue Image"/>
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
      venueName: '',
      place: '',
      capacity: '',
      rating: '',
      uploadImage: null,
      createdVenue: null,
    };
  },
  methods: {
    handleImageUpload(event) {
      this.uploadImage = event.target.files[0];
    },
    getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
    // getImageUrl(imageName) {
    //   return `${imageName}`;
    // },
    submitForm() {
      const formData = new FormData();
      formData.append('venueName', this.venueName);
      formData.append('place', this.place);
      formData.append('capacity', this.capacity);
      formData.append('rating', this.rating);
      formData.append('upload_image', this.uploadImage);

      axios
        .post('http://127.0.0.1:5000/createVenue', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: localStorage.getItem('token')
          },
        })
        .then((response) => {
          this.createdVenue = response.data;
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

