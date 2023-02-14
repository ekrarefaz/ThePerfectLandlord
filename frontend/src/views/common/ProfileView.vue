<template>
    <div class="user-card">
        <span class="avatar-holder">
          <img src="https://images.unsplash.com/photo-1527980965255-d3b416303d12?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxNDU4OXwwfDF8cmFuZG9tfHx8fHx8fHx8MTY0Mzk4NjU1Mw&ixlib=rb-1.2.1&q=80&w=200" alt="Avatar">
        </span>
        <span class="user-info-holder">
          <h2 class="name">James James</h2>
          <span class="skill">Renter</span>
      
          <div class="evaluations">
            <span class="stars evaluation">
              <span class="star-icon evaluation-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
                  <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z" />
                </svg>
              </span>
              <span class="star-text evaluation-text">4.7 Rating</span>
            </span>
          </div>
          <span class="desc">
            <p>James James has been making video games for a living for 3 years.</p>
          </span>
        </span>
      </div>
</template>

<script>

</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.user-card {
  margin: auto;
  max-width: 31.25rem;
  height: auto;
  display: flex;
  align-self: center;
  justify-content: center;
  padding: 2rem;
  background: #fff;
  border-radius: 0.5rem;
  gap: 1rem;
  box-shadow: 0px 0px 10px #80808080;
}

.avatar-holder img {
  width: 7rem;
  height: 7rem;
  border-radius: 50%;
  background: #e6effa;
  padding: 0.5rem;
  position: relative;
  display: block;
  object-fit: cover;
}

.user-info-holder {
  display: flex;
  justify-content: center;
  flex-direction: column;
  gap: 0.5rem;
}

.name {
  font-size: 1.625rem;
  color: #1c2b62;
  font-weight: bold;
  font-family: "Merriweather", sans-serif;
}

.skill {
  font-size: 1rem;
  color: #1c2b62;
}

.evaluations {
  padding: 0.5rem 0;
  display: flex;
  justify-content: center;
  flex-direction: column;
  gap: 0.5rem;
  color: #1c2b62;
}

.evaluation-icon svg {
  width: 2rem;
  height: 2rem;
  vertical-align: middle;
}

.desc {
  color: #1c2b62;
  font-weight: 300;
}

.show-more-btn {
  padding: 0.5rem 1rem;
  background: transparent;
  border: 1px solid #1c2b62;
  font-size: 1rem;
  font-weight: 600;
  color: #1c2b62;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.25s ease 0s;
}

.show-more-btn:hover,
.show-more-btn:focus {
  background: #1c2b62;
  color: #fff;
}
</style>