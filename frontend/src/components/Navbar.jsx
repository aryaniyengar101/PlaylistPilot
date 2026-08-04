function Navbar() {
  return (
    <nav className="fixed top-0 left-0 w-full z-50">

      <div
        className="
        max-w-7xl
        mx-auto
        px-12
        py-8
        flex
        justify-between
        items-center
        "
      >

        {/* Logo */}

        <h1
          className="
          text-4xl
          font-black
          tracking-tight
          cursor-pointer
          "
        >
          Playlist<span className="text-green-500">Pilot</span>
        </h1>

        {/* Navigation */}

        <div className="flex items-center gap-10">

          <button
            className="
            text-gray-400
            hover:text-white
            transition
            "
          >
            Home
          </button>

          <button
            className="
            text-gray-400
            hover:text-white
            transition
            "
          >
            About
          </button>

          <button
            className="
            px-6
            py-3
            rounded-full
            border
            border-[#30363D]
            hover:border-green-500
            hover:text-green-500
            transition-all
            duration-300
            "
          >
            Login
          </button>

        </div>

      </div>

    </nav>
  );
}

export default Navbar;