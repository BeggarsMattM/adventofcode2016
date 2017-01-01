defmodule Assembunny do

  def process(registers, {:cpy, val, reg}, pos) do
    if Map.has_key?(registers, val) do
      {%{ registers | reg => registers[val] }, pos + 1}
    else
      {%{ registers | reg => val }, pos + 1}
    end
  end

  def process(registers, {:inc, reg}, pos) do
    {%{ registers | reg => registers[reg] + 1 }, pos + 1}
  end

  def process(registers, {:dec, reg}, pos) do
    {%{ registers | reg => registers[reg] - 1 }, pos + 1}
  end

  def process(registers, {:jnz, val, jump}, pos) do
    cond do
      is_integer(val) && val > 0 ->
        {registers, pos + jump}
      is_atom(val) && registers[val] > 0 ->
        {registers, pos + jump}
      true ->
        {registers, pos + 1}
    end
  end

  def execute(registers, code, pos) when pos >= length(code) do
    registers
  end
  def execute(registers, code, pos) do
    {registers, newpos} = process(registers, Enum.at(code, pos), pos)
    execute(registers, code, newpos)
  end

end
