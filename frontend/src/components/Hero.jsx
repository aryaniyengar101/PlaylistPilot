import Waveform from "./Waveform";  
import FloatingLogo from "./FloatingLogo";
import PromptBox from "./PromptBox";

function Hero() {
  return (
    <section className="relative z-10 flex min-h-[72vh] items-center justify-center px-6">

      <div className="mx-auto flex w-full max-w-5xl flex-col items-center text-center">

        <FloatingLogo />

        <h1 className="mt-6 text-6xl font-black tracking-tight text-white md:text-7xl">
          PlaylistPilot
        </h1>

        <p className="mt-4 text-xl font-medium text-green-400">
          Playlists for every moment.
        </p>

        <p className="mt-5 max-w-2xl text-lg leading-8 text-gray-300">
          Tell us the moment.
          We'll find the music.
        </p>

        <div className="mt-10 w-full max-w-3xl">
          <PromptBox />
        </div>

      </div>

    </section>
  );
}

export default Hero;