import background from "../assets/backgrounds/rainy-tokyo.jpg";

function Background() {
  return (
    <>
      {/* Background */}
      <div className="fixed inset-0 -z-50 overflow-hidden">

        <img
          src={background}
          alt="Rainy Tokyo"
          className="
absolute
inset-0
w-full
h-full
object-cover
object-center
scale-100
brightness-[0.90]
contrast-125
saturate-95
blur-[0.8px]
transition-all
duration-700
select-none
pointer-events-none
"
        />

      </div>

      {/* Dark Overlay */}
      <div
  className="
    fixed
    inset-0
    -z-40
    bg-gradient-to-b
    from-[#090d14]/45
    via-[#090d14]/18
    to-transparent
  "
/>


      {/* Blue Overlay */}
      <div className="fixed inset-0 -z-30 bg-gradient-to-b from-[#08131d]/10 via-transparent to-[#08131d]/70" />

      {/* Green Ambient Glow */}
      <div className="hero-glow fixed -z-20" />

      {/* Vignette */}
      <div className="fixed inset-0 -z-10 bg-[radial-gradient(circle_at_center,transparent_10%,rgba(0,0,0,.15)_55%,rgba(0,0,0,.65)_100%)]" />
    </>
  );
}

export default Background;