<script>
	export let open = false
</script>

<aside class="bg-cyan-600 text-cyan-100 w-64 space-y-6 px-2 py-4 absolute inset-y-0" class:open>
    <div>
        <br>
        <br>
        <a href="/" class="flex items-center space-x-2 py-3 px-4 hover:bg-cyan-700"><span class="text-white">아침 메뉴</span></a>
        <a href="/" class="flex items-center space-x-2 py-3 px-4 hover:bg-cyan-700"><span class="text-white">점심 메뉴</span></a>
        <a href="/" class="flex items-center space-x-2 py-3 px-4 hover:bg-cyan-700"><span class="text-white">저녁 메뉴</span></a>
    </div>
</aside>
<style>
	aside {
		left: -100%;
		transition: left 0.3s ease-in-out
	}
	
	.open {
		left: 0
	}
</style>