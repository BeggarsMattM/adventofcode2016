defmodule RC do
  def is_numeric(str) do
    case Float.parse(str) do
      {_num, ""} -> true
      {_num, _r} -> false               # _r : remainder_of_binary
      :error     -> false
    end
  end
end

defmodule Day12Elixir do

import Assembunny

def input, do: """
cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5
"""

def code do
 input |> String.split("\n")
       |> Enum.reject(fn x -> x == "" end)
       |> Enum.map(&String.split/1)
       |> Enum.map(fn x ->
         Enum.map(x, fn x ->
          if RC.is_numeric(x) do
            String.to_integer(x)
          else
            String.to_atom(x)
          end
        end)
      end)
     |> Enum.map(&List.to_tuple/1)
end

def registers, do: %{a: 0, b: 0, c: 0, d: 0}

def part1 do
  execute(registers, code, 0)
end

def part2 do
  execute(%{a: 0, b: 0, c: 1, d: 0}, code, 0)
end

end
