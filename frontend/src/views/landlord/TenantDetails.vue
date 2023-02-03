<template>
    <h1>Details</h1>
    <div v-if="tenant">
        <div class="tenant-container">
            <div class="tenant-title">
                <img src="../../assets/logo.png" alt="">
                <h2 class="title">{{ tenant.name }}</h2>
            </div>
            <div class="tenant-details">
                <div class="details">
                    <p><strong>Age: </strong>{{tenant.age}}</p>
                    <p><strong>Gender: </strong>{{tenant.age}}</p>
                    <p><strong>Occupation: </strong>{{ tenant.job }}</p>
                </div>
                <div class="preferences">
                    <p><strong>Apartment Type: </strong>{{tenant.preference.type}}</p>
                    <p><strong>Parking Required: </strong>{{tenant.preference.parking}}</p>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        props: ['id'],
        data(){
            return{
                tenant: null
            }
        },
        mounted(){
            fetch('http://localhost:3000/tenants/' + this.id)
            .then(res => res.json())
            .then(data => this.tenant = data)
            .catch(err => console.log(err.message))
        }
    }
</script>

<style scoped>
.tenant-container{
    margin: 50px;
    display: flex;
    align-content: space-around;
    border: 2px solid black;
}
.tenant-title{
    padding: 50px;
}
.tenant-details{
    padding: 50px;
    display: flex;
    align-content: space-between;
    border: 1px solid navy;
}
.details, .preferences{
    padding: 30px;
    border: 2px solid black;
}
</style>