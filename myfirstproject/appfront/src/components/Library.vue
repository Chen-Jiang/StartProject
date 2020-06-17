<template>
  <div class="home">
    <div display="margin-top:10px">
        <input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left">
        <button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</button>
    </div>

    <div id="Home">
    <ul>
      <li v-for="item in bookList">
        {{item.book_name}}
      </li>

    </ul>
    </div>

  </div>
</template>


<script>
  export default {
      name: 'Home',
      // el: "#Home",
      data() {
          return {
              input: '',
              bookList: []
          }
      },
      mounted: function () {
          this.showbooks()
      },
      methods: {
          addBook() {
              this.$http.get('http://127.0.0.1:8000/myapp/add_book?book_name='+this.input)
                  .then((response) => {
                      var res = JSON.parse(response.bodyText);
                      if (res['error_num'] === 0) {
                          this.showbooks()
                      } else {
                          this.$message.error('Somgthing wrong...');
                          console.log(res['msg'])
                      }
                  })
          },
          showbooks() {
              this.$http.get('http://127.0.0.1:8000/myapp/show_books')
                  .then((response) => {
                      var res = JSON.parse(response.bodyText);
                      console.log("res", res);
                      console.log("num", res['error_num']);
                      if (res['error_num'] === 0) {
                          this.bookList = res['list'];
                          // console.log(this.bookList)
                      } else {
                          this.$message.error('Something wrong...');
                          console.log("mmsg", res['msg']);
                      }
                  })
          }
      }
  }
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
