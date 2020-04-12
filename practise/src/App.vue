<template>
<div id='app' class="container">
  <h2>我的购物车列表</h2>
  <div class="input-group">
    <input type="text" placeholder="输入你想购买的物品" class='js-new-item form-control' required>
    <span class="input-group-btn">
        <button type="button" class="js-add btn btn-default">添加到购物车</button>
    </span>
  </div>
  <ul>
    <li>
      <div class="checkbox">
        <label for="">
          <input type="checkbox" class="js-item"> 苹果
        </label>
      </div>
    </li>
    <li>
      <div class="checkbox">
        <label for="">
          <input type="checkbox" class="js-item"> 香蕉
        </label>
      </div>
    </li>
    <li>
      <div class="checkbox">
        <label for="">
          <input type="checkbox" class="js-item"> 橘子
        </label>
      </div>
    </li>
  </ul>
  <!-- 修改标题 -->
  <div class='footer'>
    <hr>
    <span>改变标题</span>
    <input type="text" class='js-change-title' value='我的购物车列表'>
  </div>
</div>
</template>

<script>

</script>

<style>
.container{
    width: 50%;
    margin: 100px auto;
}
.removed{
    color: grey;
}
.removed label{
    text-decoration: line-through;
}
ul{
    border: 1px solid black;
    margin-top: 30px;
}
ul li{
    list-style: none;
}
</style>
