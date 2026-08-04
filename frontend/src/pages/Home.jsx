import Background from "../components/Background";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import FeatureCards from "../components/FeatureCards";

function Home() {
  return (
    <div className="relative min-h-screen">

      <Background />

      <Navbar />

      <main className="relative z-10">

        <Hero />

        <div className="max-w-6xl mx-auto px-6">

          <FeatureCards />

        </div>

      </main>

    </div>
  );
}

export default Home;