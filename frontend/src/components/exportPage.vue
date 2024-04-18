<template>
    <div>
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Export Data</h5>
                <p class="card-text">Export your data in CSV format</p>
            </div>
        </div>
        <div id="divToPrint" class="mt-5">
            <h4>Venue Details</h4>
            <div class="table-responsive">
                <table class="table table-bordered" >
                    <!-- @click="printDocument()" -->

                    <thead>
                        <tr>
                            <th>Show name</th>
                            <th>Date</th>
                            <th>Movie tag</th>
                            <th>Ticket price</th>
                            <th>Tickets booked</th>
                            <th>Rating</th>
                            
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="show in shows" :key="show.id">
                            <td>{{ show?.name }}</td>
                            <td>{{ show?.date }}</td>
                            <td>{{ show?.tags }}</td>
                            <td>{{ show?.ticket }}</td>
                            <td>{{ show?.tickets_booked }}</td>
                            <td>{{ show?.rating }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="mt-5 text-center">
            <h2>Export data to CSV</h2>
            <button class="btn btn-primary" @click="exportData">Download CSV file</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    
    data() {
        return {
            venues: [],
            shows: []
        }
    },
    mounted(){
        this.getDetails()
    },

    methods: {
        

        getDetails(){
            const venueID = this.$route.params.venueID;
            const apiurl = `http://127.0.0.1:5000/export/${venueID}/` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.venues = response.data.venues
                this.shows=response.data.shows;
                console.log(this.shows)
            })
          .catch(error=> console.error('error :',error));

        },
        exportData() {
            const csvContent = this.convertDataToCSV(this.shows);

            // Create a Blob containing the CSV data
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });

            // Create a data URI for the Blob
            const dataURI = URL.createObjectURL(blob);

            // Create an anchor element and set its attributes
            const link = document.createElement('a');
            link.href = dataURI;
            link.download = 'venue_data.csv';

            // Append the link to the document and click it to trigger the download
            document.body.appendChild(link);
            link.click();

            // Clean up by removing the link from the document
            document.body.removeChild(link);
         },
         convertDataToCSV(data) {
            const header = 'Show name,Date,Movie tag,Ticket price,Tickets booked,Rating\n';
            const csvRows = data.map(show => `${show.name},${show.date},${show.tags},${show.ticket},${show.tickets_booked},${show.rating}`).join('\n');
            return header + csvRows;
        },
    },

    
}
</script>

<style></style>