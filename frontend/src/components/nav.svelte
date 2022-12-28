<script>
    import Bar from "./bar.svelte";
    let open = false;

    function setup() {
        open = !open;
    }
</script>
<Bar bind:open class="absolute"></Bar>
<div class="relative flex min-h-screen">

    <div class="flex-1">
        <div class="flex bg-white shadow px-2 py-4">
            <button on:click={setup} class="text-cyan-600 font-extrabold">
                <svg style="margin-left: 10px" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
            </button>
            <span style="padding-left: 30px" class="text-2xl font-extrabold text-blue-800">BACKDOOR 음식 메뉴 정해주는 사이트</span>
        </div>
    </div>
</div>