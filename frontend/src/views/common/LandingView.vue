<template>
<body>
    <div v-show="loaded">
        <LoadingAnimated/>
    </div>
        <main>
            <NavBar/>
            <div class="content">
            <span>marketplace</span>
            <h1>The Perfect Landlord</h1>
            <p>matchmaking platform for landlord and tenants</p>
            <ol>
                <li>Tell us your preferences</li>
                <li>Get matched with your realestate soulmate</li>
                <li>Let us handle all the paperworks</li>
                <li>Close your membership anytime!</li>
            </ol>
            </div>
            <div class="img-container">
            <img src="../../assets/rental_bg.jpg" alt="">
            <div class="order">
                <div>
                <span>Membership</span>
                <div class="price"><span>$</span>
                    <h2>9.99</h2>/month
                </div>
                </div>
                <hr>
                <div>
                    <router-link :to="{name: 'signup'}">Join Now</router-link>
                </div>
            </div>
            </div>
        </main>
</body>
</template>

<script>
    import NavBar from '../../components/NavBar.vue'
    import LoadingAnimated from '../../components/LoadingAnimated.vue'
    export default{
        data(){
            return{
                loaded: true
            }
        },
        components: {
            NavBar,
            LoadingAnimated,
        },
        created(){
            setTimeout(()=> this.loaded = false, 2000)
        }
    }
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  body {
    background: black;
    margin: 0;
    display: grid;
    min-height: 100vh;
    font-family: 'Poppins', sans-serif;
    font-weight: 300;
    width: 100%;
    height: 100%;
  }
  main {
    background: whitesmoke;
    overflow: hidden;
    display: flex;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.161);
    flex-direction: column-reverse;
    width: 100vw;
    height: 100vh;
  }
  @media screen and (min-width: 900px) {
    main {
      flex-direction: row;
    }
  }
  main .content {
    padding: 3em 2em;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  @media screen and (min-width: 900px) {
    main .content {
      padding: 5em 4.5em;
    }
  }
  main .content a {
    text-decoration: none;
    color: #838383;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
  }
  main .content a:hover {
    color: #eb8a88;
  }
  main .content span {
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 0.125rem;
    color: #00801d;
    font-weight: 500;
  }
  main .content h1 {
    text-transform: capitalize;
    font-size: clamp(1.5rem, 5vw, 4rem);
    font-family: 'Comfortaa';
    font-weight: 700;
    margin: 0.2em 0 0.6rem 0;
  }
  main .content p {
    max-width: 350px;
  }
  main .content svg {
    width: 26px;
    margin-right: 10px;
  }
  main .img-container {
    width: 100%;
    position: relative;
    min-height: 380px;
    height: 30vh;
  }
  @media screen and (min-width: 900px) {
    main .img-container {
      height: auto;
    }
  }
  main img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  main .order {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    padding: 2em 2em;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.161);
    height: min-content;
  }
  @media screen and (min-width: 600px) {
    main .order {
      width: 80%;
      display: flex;
    }
  }
  @media screen and (min-width: 900px) {
    main .order {
      min-width: 360px;
      width: auto;
      top: 50%;
      left: 75%;
      transform: translate(-75%, -50%);
      padding: 3em 2.8em;
      display: block;
    }
  }
  main .order p {
    color: #6b6b6b;
    max-width: 200px;
  }
  main .order a {
    display: inline-block;
    background: #000;
    color: #fff;
    display: inline-block;
    padding: 0.7em 2.2em;
    border-radius: 60px;
    text-transform: capitalize;
    text-decoration: none;
    margin-top: 2em;
    font-size: 0.9rem;
  }
  main .order a:hover {
    background: #cd7786;
  }
  @media screen and (min-width: 900px) {
    main .order a {
      font-size: 1rem;
    }
  }
  main .order span {
    font-size: 1.3rem;
  }
  @media screen and (min-width: 900px) {
    main .order span {
      font-size: 1.5rem;
    }
  }
  main .order .price {
    display: flex;
    align-items: flex-end;
    font-size: 1rem;
    margin: 15px;
  }
  main .order .price span {
    font-size: 1.5rem;
    margin-bottom: -3px;
    font-weight: 300;
  }
  @media screen and (min-width: 900px) {
    main .order .price span {
      font-size: 2.5rem;
      margin-bottom: -10px;
    }
  }
  main .order .price h2 {
    font-size: 2.2rem;
    font-weight: 700;
    margin-bottom: -10px;
    margin-inline: 5px;
  }
  @media screen and (min-width: 900px) {
    main .order .price h2 {
      font-size: 3rem;
      margin-bottom: -15px;
    }
  }
  main hr {
    background: #cecece;
    width: 30%;
    height: 1px;
    border: none;
    display: block;
    margin: 4em 0 1em 0;
  }
  @media screen and (min-width: 600px) {
    main hr {
      transform: rotate(90deg);
    }
  }
  @media screen and (min-width: 900px) {
    main hr {
      transform: rotate(0deg);
    }
  }
  ol {
    list-style: none;
    margin: 0;
    padding: 0;
    counter-reset: section;
    z-index: 1;
    margin: 2em 0 2.5em 0;
  }
  li {
    display: flex;
    align-items: center;
    position: relative;
  }
  li+li {
    margin-top: 1em;
  }
  li::before {
    counter-increment: section;
    content: counters(section, '.') ' ';
    background: #000;
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    min-width: 26px;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    font-size: 0.9rem;
    font-weight: 200;
    margin-right: 1em;
    position: relative;
    z-index: 66;
  }
  li:not(:last-child):after {
    content: '';
    width: 1px;
    height: 200%;
    background: #000;
    position: absolute;
    left: 12.5px;
    top: 50%;
  }
  
</style>