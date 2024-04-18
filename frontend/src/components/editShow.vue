<template>
  <div>
    <h1>Edit Show</h1>
    <form @submit.prevent="submitForm">
      <!-- Show Name -->
      <label for="name">Show Name:</label>
      <input type="text" id="name" v-model="shows.name" required />

      <!-- Show Tags -->
      <label for="tags">Tags:</label>
      <input type="text" id="tags" v-model="shows.tags" required />

      <!-- Show date  -->
      <label for="date">Date:</label>
      <input type="date" id="date" v-model="shows.date" required />

      <!-- Show Ticket -->
      <label for="ticket">Ticket Price:</label>
      <input type="number" id="ticket" v-model="shows.ticket" required />
      
      
      <!-- Show Rating -->
      <label for="rating">Rating:</label>
      <input type="number" id="rating" v-model="shows.rating" required />

      <!-- Show Image -->
      <label for="upload_image">Image:</label>
      <input type="file" id="upload_image" name="upload_image" @change="handleImageUpload" required />

      <button type="submit">Submit</button>
    </form>

    <!-- Display the created show -->
    <div v-if="createdShow">
      <h2>Created Show:</h2>
      <p>Name: {{ createdShow.name }}</p>
      <p>Tags: {{ createdShow.tags }}</p>
      <p>Date: {{ createdShow.date }}</p>
      <p>Price: {{ createdShow.ticket }}</p>
      <p>Rating: {{ createdShow.rating }}</p>
      <img :src="getImageUrl(createdShow.img)" alt="Show Image" />
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
      shows: {}, 
    };
  },
  mounted() {
    // Fetch data after the component is mounted
    this.getShows();
  },
  methods: {
    handleImageUpload(event) {
      this.uploadImage = event.target.files[0];
    },
    getImageUrl(imageName) {
      return `${imageName}`;
    },
    getShows() {
      const showID = this.$route.params.showID;
      const apiurl = `http://127.0.0.1:5000/updateShow/${showID}/`;
      axios
        .get(apiurl, {
          headers: {
            Authorization: localStorage.getItem('token')
          }
        })
        .then((response) => {
          this.shows = response.data;
        })
        .catch((error) => console.error('error :', error));
    },
    submitForm() {
      const formData = new FormData();
      formData.append('name', this.shows.name);
      formData.append('tags', this.shows.tags);
      formData.append('date', this.shows.date);
      formData.append('ticket', this.shows.ticket);
      formData.append('rating', this.shows.rating);
      formData.append('upload_image', this.uploadImage);

      const showID = this.$route.params.showID;
      const apiurl = `http://127.0.0.1:5000/updateShow/${showID}/`;
      console.log(formData)

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


