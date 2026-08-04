import { ArrowUp, Heart, Dumbbell, Clock3 } from "lucide-react";

function PromptBox() {
  return (
    <div
      className="
        rounded-[30px]
        border
        border-white/10
        bg-white/[0.06]
        backdrop-blur-2xl
        shadow-[0_10px_60px_rgba(0,0,0,.25)]
        p-5
      "
    >
      <textarea
        rows="2"
        placeholder="Tell us your story..."
        className="
          w-full
          resize-none
          bg-transparent
          outline-none
          text-white
          placeholder:text-gray-400
          text-lg
        "
      />

      <div className="mt-4 flex items-center justify-between">

        <div className="flex gap-3 flex-wrap">

          <button className="chip">
            <Heart size={16} />
            Romantic
          </button>

          <button className="chip">
            <Dumbbell size={16} />
            Gym
          </button>

          <button className="chip">
            <Clock3 size={16} />
            Memories
          </button>

        </div>

        <div className="flex items-center gap-3">

          <select
            className="
              rounded-full
              bg-white/5
              px-4
              py-2
              text-sm
              outline-none
            "
          >
            <option>10 Songs</option>
            <option>20 Songs</option>
            <option>30 Songs</option>
            <option>50 Songs</option>
          </select>

          <button
            className="
              flex
              h-11
              w-11
              items-center
              justify-center
              rounded-full
              bg-green-500
              transition
              hover:scale-105
            "
          >
            <ArrowUp size={18} />
          </button>

        </div>

      </div>
    </div>
  );
}

export default PromptBox;