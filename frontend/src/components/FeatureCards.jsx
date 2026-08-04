import {
  Brain,
  Music2,
  CloudRain,
  BadgeCheck,
} from "lucide-react";

const cards = [
  {
    icon: <Brain size={22} />,
    title: "AI Playlist Creation",
    description:
      "Describe your mood, activity or memory and let AI build the perfect soundtrack.",
  },
  {
    icon: <Music2 size={22} />,
    title: "Spotify Connected",
    description:
      "Save playlists directly to Spotify with one click after generation.",
  },
  {
    icon: <CloudRain size={22} />,
    title: "Weather Reactive",
    description:
      "Coming soon — playlists that adapt to the weather around you.",
  },
  {
    icon: <BadgeCheck size={22} />,
    title: "Music Passport",
    description:
      "Build your music journey by saving memories and revisiting playlists.",
  },
];

function FeatureCards() {
  return (
    <section className="relative mt-10 pb-16">

      {/* Subtle Overlay */}
      <div
        className="
          absolute
          inset-0
          -z-10
          rounded-3xl
          bg-gradient-to-b
          from-transparent
          via-[#081018]/10
          to-[#081018]/35
          backdrop-blur-sm
        "
      />

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-7">

        {cards.map((card, index) => (
          <div
            key={index}
            className="
              group
              rounded-3xl
              p-7
              border
              border-white/10
              bg-white/[0.045]
              backdrop-blur-xl
              shadow-[0_0_40px_rgba(0,0,0,0.18)]
              transition-all
              duration-500
              hover:-translate-y-2
              hover:border-green-400/40
              hover:bg-white/[0.07]
              hover:shadow-[0_0_35px_rgba(34,197,94,.18)]
            "
          >

            <div
              className="
                w-12
                h-12
                rounded-xl
                bg-green-500/15
                border
                border-green-500/20
                flex
                items-center
                justify-center
                text-green-400
                mb-5
                transition-all
                duration-500
                group-hover:scale-110
                group-hover:bg-green-500/25
              "
            >
              {card.icon}
            </div>

            <h3 className="text-lg font-semibold mb-3 text-white">
              {card.title}
            </h3>

            <p className="text-sm leading-7 text-gray-400">
              {card.description}
            </p>

          </div>
        ))}

      </div>

    </section>
  );
}

export default FeatureCards;